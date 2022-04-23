"""def gridDataRandom(size):
    dataTarget = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        dataTarget.append(line)
    listTargetChose = []


    if size == SIZE_GRID_SMALL:
        # 1 shipM and 5 shipS

        # 1 shipM
        shipM_Added = 0
        while shipM_Added < 1:
            yShipM = random.randint(0, size-1)
            if yShipM > (size-3):
                xShipM = random.randint(0, size-3)
                horizontal = True
            else:
                horizontal = random.choice([True, False])
                if horizontal:
                    xShipM = random.randint(0, size-3)
                else:
                    xShipM = random.randint(0, size-1)
            
            if horizontal:
                canAdded = True
                for i in range(xShipM, xShipM+3):
                    if (yShipM, i) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(xShipM, xShipM+3):
                        dataTarget[yShipM][i] = 1
                        listTargetChose.append((yShipM, i))
                    shipM_Added += 1
            else:
                canAdded = True
                for i in range(yShipM, yShipM+3):
                    if (i, xShipM) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(yShipM, yShipM+3):
                        dataTarget[i][xShipM] = 1
                        listTargetChose.append((i, xShipL))
                    shipM_Added += 1      

        # 5 shipS
        shipS_Added = 0
        while shipS_Added < 5:
            xShipS = random.randint(0, 6)
            yShipS = random.randint(0, 6)
            if (yShipS, xShipS) not in listTargetChose:
                dataTarget[yShipS][xShipS] = 1
                shipS_Added += 1
                listTargetChose.append((yShipS, xShipS))


    if size == SIZE_GRID_MEDIUM:
        # 1 shipL and 2 shipM and 5 shipS

        # 1 shipL
        shipL_Added = 0
        while shipL_Added < 1:
            yShipL = random.randint(0, size-1)
            if yShipL > (size-5):
                xShipL = random.randint(0, size-5)
                horizontal = True
            else:
                horizontal = random.choice([True, False])
                if horizontal:
                    xShipL = random.randint(0, size-5)
                else:
                    xShipL = random.randint(0, size-1)
            
            if horizontal:
                canAdded = True
                for i in range(xShipL, xShipL+5):
                    if (yShipL, i) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(xShipL, xShipL+5):
                        dataTarget[yShipL][i] = 1
                        listTargetChose.append((yShipL, i))
                    shipL_Added += 1
            else:
                canAdded = True
                for i in range(yShipL, yShipL+5):
                    if (i, xShipL) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(yShipL, yShipL+5):
                        dataTarget[i][xShipL] = 1
                        listTargetChose.append((i, xShipL))
                    shipL_Added += 1


        
        # 2 shipM
        shipM_Added = 0
        while shipM_Added < 2:
            yShipM = random.randint(0, size-1)
            if yShipM > (size-3):
                xShipM = random.randint(0, size-3)
                horizontal = True
            else:
                horizontal = random.choice([True, False])
                if horizontal:
                    xShipM = random.randint(0, size-3)
                else:
                    xShipM = random.randint(0, size-1)
            
            if horizontal:
                canAdded = True
                for i in range(xShipM, xShipM+3):
                    if (yShipM, i) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(xShipM, xShipM+3):
                        dataTarget[yShipM][i] = 1
                        listTargetChose.append((yShipM, i))
                    shipM_Added += 1
            else:
                canAdded = True
                for i in range(yShipM, yShipM+3):
                    if (i, xShipM) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(yShipM, yShipM+3):
                        dataTarget[i][xShipM] = 1
                        listTargetChose.append((i, xShipM))
                    shipM_Added += 1

        
        # 5 shipS
        shipS_Added = 0
        while shipS_Added < 5:
            xShipS = random.randint(0, 6)
            yShipS = random.randint(0, 6)
            if (yShipS, xShipS) not in listTargetChose:
                dataTarget[yShipS][xShipS] = 1
                listTargetChose.append((yShipS, xShipS))
                shipS_Added += 1

    res = []
    for line in dataTarget:
        for data in line:
            res.append(data)

    return res"""