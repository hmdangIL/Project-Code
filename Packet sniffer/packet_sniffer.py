######################### IMPORT LIBRARIES ############################

from distutils.log import error
import socket
import struct
import sys
import argparse
import textwrap


####################### PRINT IN FORMAT MULTI-LINE #####################

def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

TAB_1 = '\t'
TAB_2 = '\t\t'
TAB_3 = '\t\t\t'
TAB_4 = '\t\t\t\t'

################# CREATE SOCKET FOR THE CONNECTION DEMO #################
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)           #this line sniff only TCP packet
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)           #this line sniff only UDP packet
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)          #this line sniff only ICMP packet
#s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))    #this line sniff all packet

#################### PARSE THE ETHERNET HEADER ##########################

def ethernet_head(raw_data):
    dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])
    dest_mac = get_mac_addr(dest)
    src_mac = get_mac_addr(src)
    proto = socket.htons(prototype)
    data = raw_data[14:]
    return dest_mac, src_mac, proto, data

def get_mac_addr(addr):
    byte_str = map('{:02x}'.format, addr)
    mac_addr = ':'.join(byte_str).upper()
    return mac_addr

######################## PARSE THE IPV4  ################################

def ipv4_head(raw_data):
    version_header_length, tos, total_len, identification, flags_offset, ttl, proto, header_checksum, src, target = struct.unpack('! B B H H H B B H 4s 4s', raw_data[:20])  
    # ttl - time to live; tos - type of service
    # extracting x_bit, do not fragment flag and more fragments follow flag
    version = version_header_length >> 4                  # shifted to the right by 4 places
    header_length = (version_header_length & 15)          # bitwise logical operator with 15 = 0000 1111
    x_bit =  (flags_offset >> 15) & 1 
    DFF   =  (flags_offset >> 14) & 1
    MFF   =  (flags_offset >> 13) & 1
    # extracting fragment offset
    frag_offset = flags_offset & 8191
    data = raw_data[20:]
    return version, header_length, tos, total_len, identification, x_bit, DFF, MFF, frag_offset, ttl, proto, header_checksum, get_ip(src), get_ip(target), data

def get_ip(addr):
    ip_addr = '.'.join(map(str, addr))
    return ip_addr

########################## PARSE THE TCP ################################

def tcp_head(raw_data):
    (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags) = struct.unpack('! H H L L H', raw_data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    data = raw_data[offset:]
    return src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data

########################## PARSE THE ICMP HEADER #######################

def icmp_head(raw_data):
    type, code, checksum = struct.unpack('! B B H', raw_data[:4])
    data = raw_data[4:]
    return type, code, checksum, data

########################## PARSE THE ICMP HEADER #######################

def udp_head(raw_data):
    src, target, length, checksum = struct.unpack('! H H 2x H', raw_data[:8])
    data = raw_data[8:]
    return src, target, length, checksum, data

########################## DECODE HTTP DATA #############################

"""def http(raw_data):
    try:
        data = raw_data.decode(encoding="utf-8")
    except:
        data = raw_data
    return data
"""

############################ MAIN FUNCTION ##############################

def main():
    # create raw socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    # infinity loop to process the program
    while True:
        raw_data, addr = s.recvfrom(65535)
        eth = ethernet_head(raw_data)
        # information of Ethernet Frame
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(eth[0], eth[1], eth[2]))
        # take the data of ethernet frame
        # information IPv4 if protocol 8 (Exterior Gateway Protocol) 
        if eth[2] == 8:
            ipv4 = ipv4_head(eth[4])
            print( '\t - ' + 'IPv4 Packet:')
            print('\t\t - ' + 'Version: {}, Header Length: {}, TOS: {}, Total Length: {}'.format(ipv4[0], ipv4[1], ipv4[2], ipv4[3]))
            print('\t\t - ' + 'ID: {}, Flags: {}|{}|{}, Fragment Offset: {}, TTL: {}'.format(ipv4[4], ipv4[5], ipv4[6], ipv4[7], ipv4[8], ipv4[9]))
            print('\t\t - ' + 'Protocol: {}, Checksum: {}, Source IP: {}, Destination IP: {}'.format(ipv4[10], ipv4[11], ipv4[12]))
            # TCP - protocol 6 
            if ipv4[4] == 6:
                tcp = tcp_head(ipv4[7])
                print(TAB_1 + 'TCP Segment:')
                print(TAB_2 + 'Source Port: {}, Destination Port: {}'.format(tcp[0], tcp[1]))
                print(TAB_2 + 'Sequence: {}, Acknowledgment: {}'.format(tcp[2], tcp[3]))
                print(TAB_2 + 'Flags:')
                print(TAB_3 + 'URG: {}, ACK: {}, PSH:{}'.format(tcp[4], tcp[5], tcp[6]))
                print(TAB_3 + 'RST: {}, SYN: {}, FIN:{}'.format(tcp[7], tcp[8], tcp[9]))
                # print data packet if len(data) > 10
                if len(tcp[10]) > 0:
                    # port HTTP
                    if tcp[0] == 80 or tcp[1] == 80:
                        print(TAB_2 + 'HTTP Data:')
                        try:
                            # http = http(tcp[10])
                            http = tcp[10]
                            http_info = str(http[10]).split('\n')
                            for line in http_info:
                                print(TAB_3 + str(line))
                        except:
                            print(format_multi_line(TAB_3, tcp[10]))
                    # else this is TCP data
                    else:
                        print(TAB_2 + 'TCP Data:')
                        print(format_multi_line(TAB_3, tcp[10]))
            # ICMP (Internet Control Message)
            elif ipv4[4] == 1:
                icmp = icmp_head(ipv4[7])
                print('\t -' + 'ICMP Packet:')
                print('\t\t -' + 'Type: {}, Code: {}, Checksum:{},'.format(icmp[0], icmp[1], icmp[2]))
                print('\t\t -' + 'ICMP Data:')
                print(format_multi_line('\t\t\t', icmp[3]))
            # UDP (User Datagram Protocol)
            elif ipv4[4] == 17:
                udp = udp_head(ipv4[7])
                print('\t -' + 'UDP Segment:')
                print('\t\t -' + 'Source Port: {}, Destination Port: {}, Length: {}, Checksum: {}'.format(udp[0], udp[1], udp[2], udp[3]))
                print('\t\t -' + 'UDP Data:')
                print(format_multi_line('\t\t\t', udp[4]))
            # Other IPv4
            else:
                print('\t -' + 'Other IPv4 Data:')
                print(format_multi_line('\t\t', ipv4[7]))
        else:
            print('Ethernet Data:')
            print(format_multi_line('\t', eth[3]))



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("Aborting packet capture...")