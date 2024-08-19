def part01():
    with open('day11.txt', 'rt') as myFile:
        data = myFile.read().splitlines()
    myString=''
    myList=[]
    tempList=[]
    for i in data:
        if i != '':
            myString+=i
        elif i == '':
            myList.append(myString)
            myString=''
    # print('@@@@@@@@@@@@@@@@@@@@', myList, '@@@@@@@@@@@@@@@@@@@@')
    monkeyList = []
    for i in myList:
        monkeyNo = []
        startingItems = []
        operation = []
        test = []
        throwTo = []
        
        for j in i.split('  ')[0]:
            if j.isdigit() == True:
                monkeyNo.append(int(j))
        temp = ''
        for j in i.split('  ')[1]:
            temp += j
        startingItems = temp[16:].split(',')
        temp = ''
        for j in i.split('  ')[2]:
            temp += j
            operation = temp[21:].split(' ')
        test.append(int(i.split('  ')[3][18:]))
        # print(test)
        throwTo.append(int(i.split('  ')[5][24:]))
        throwTo.append(int(i.split('  ')[7][25:]))
        # print(throwTo)

        
        monkeytemp = []
        monkeytemp.append(monkeyNo)
        monkeytemp.append(startingItems)
        monkeytemp.append(operation)
        monkeytemp.append(test)
        monkeytemp.append(throwTo)

        monkeyList.append(monkeytemp)
    
    myDict = {
        0: [],
        1: [],
        2: [],
        3: []
        }
    # for z in range(2):
    for i in monkeyList:
        for l in myDict.items():
            if sum(i[0]) == l[0]:
                print(l, '^^^^^^^^^^')
                i[1].extend(l[1])
                l[1].clear()
                print(l, '^^^^^^^^^^')
        print("This monkey's turn: ", sum(i[0]), '***********')
        print(i, '##########')
        for j in i[1]:
            # print(int(j))
            # x = 0
            # FOR MULTIPLICATION OPERATOR
            if i[2][0] == '*':
                if i[2][1] == 'old':
                    x = int(j) * int(j)
                    x = int(x/3)
                    # CHECKING TEST IF NUMBER IS DIVISIBLE?
                    # IF TRUE
                    if x % i[3][0] == 0:
                        # print(i[4][0])
                        for k in myDict.keys():
                            if i[4][0] == k:
                                print(j, k, '-----**----')
                                myDict[k].append(j)
                                print(myDict)
                    # IF FALSE
                    else:
                        # print(i[4][1])
                        for k in myDict.keys():
                            if i[4][1] == k:
                                print(j, k, '---------')
                                myDict[k].append(j)
                                print(myDict)
                else:
                    x = int(j) * int(i[2][1])
                    x = int(x/3)
                    if x % i[3][0] == 0:
                        # print(i[4][0])
                        for k in myDict.keys():
                            if i[4][0] == k:
                                print(j, k, '---------')
                                myDict[k].append(j)
                                print(myDict)
                    else:
                        # print(i[4][1])
                        for k in myDict.keys():
                            if i[4][1] == k:
                                print(j, k, '---------')
                                myDict[k].append(j)
                                print(myDict)
            
            if i[2][0] == '+':
                if i[2][1] == 'old':
                    x = int(j) + int(j)
                    x = int(x/3)
                    # CHECKING TEST IF NUMBER IS DIVISIBLE?
                    # IF TRUE
                    if x % i[3][0] == 0:
                        # print(i[4][0])
                        for k in myDict.keys():
                            if i[4][0] == k:
                                print(j, k, '-----**----')
                                myDict[k].append(j)
                                print(myDict)
                    # IF FALSE
                    else:
                        # print(i[4][1])
                        for k in myDict.keys():
                            if i[4][1] == k:
                                print(j, k, '---------')
                                myDict[k].append(j)
                                print(myDict)
                else:
                    x = int(j) + int(i[2][1])
                    x = int(x/3)
                    if x % i[3][0] == 0:
                        # print(i[4][0])
                        for k in myDict.keys():
                            if i[4][0] == k:
                                print(j, k, '---------')
                                myDict[k].append(j)
                                print(myDict)
                    else:
                        # print(i[4][1])
                        for k in myDict.keys():
                            if i[4][1] == k:
                                print(j, k, '---------')
                                myDict[k].append(j)
                                print(myDict)
part01()
