##################### SIMPLE PORT SCANNER #######################
"""
import socket
from colorama import init, Fore

# add color
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def is_port_open(host, post):
    s = socket.socket()
    try:
        s.connect((host, post))
    except:
        return False                        # the port is closed
    else:
        return True                         # the port is opened

host = input("Enter the host: ")
for port in range(1, 1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open {RESET}")
    else:
        print(f"{GRAY}[+] {host}:{port} is closed {RESET}", end="\r")
"""


#################### THREADED PORT SCANNER ########################

import argparse
import socket
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue

# add colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

N_THREADS = 300              # set the number of thread

q = Queue()                  # thread queue
print_lock = Lock()

def port_scan(port):
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
            print(f"{GRAY}{host:15}:{port:5} is closed {RESET}", end="\r")
    else:
        with print_lock:
            print(f"{GREEN}{host:15}:{port:5} is open {RESET}")
    finally:
        s.close()

def scan_thread():
    global q
    while True:
        worker = q.get()         # get the port number from the queue
        port_scan(worker)
        q.task_done()

def main(host, ports):
    global q
    for t in range(N_THREADS):
        t = Thread(target=scan_thread)  
        t.daemon = True          # when we set daemon to true, that thread will end when the main thread ends
        t.start()
    for worker in ports:
        q.put(worker)
    q.join()                     # wait the threads (port scanners) to finish

if __name__ == "__main__":
    # parse some parameters passed
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("--host", help="Host to scan.")
    parser.add_argument("--ports", dest="port_range", default="1-5000", help="Port range to scan, default is 1-5000")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range
    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)
    ports = [p for p in range(start_port, end_port+1)]
    try:
        main(host, ports)
    except KeyboardInterrupt:
        raise SystemExit("Aborting Port Scanner...")
