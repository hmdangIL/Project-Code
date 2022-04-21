listDT = [1, 0, 1, 2, 1, 2]
with open("testData", 'w') as data:
    for i in listDT:
        data.write(str(i) + '\n')
