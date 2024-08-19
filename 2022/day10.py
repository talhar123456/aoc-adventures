def part01():
    # file open
    with open('day10.txt', 'rt') as myFile:
        data = myFile.read().splitlines()
    # print(data)
    cycle = 1
    cycleList = [20,60,100,140,180,220]
    add = 1
    ans = []
    myDict = {}
    for i in data:
        data = i.split(' ')
        if data[0] == 'noop':
            cycle += 1
            myDict[cycle] = cycle*add
            # print('cycle', cycle, 'add', add, cycle*add, '*******')
            for j in cycleList:
                if j == cycle:
                    ans.append(cycle*add)
        if data[0] == 'addx':
            for i in range(2):
                # print(data[0], data[-1])
                # add += int(data[-1])
                cycle += 1
                myDict[cycle] = cycle*add
                # print('cycle', cycle, 'add', add, cycle*add, '-------')
            add += int(data[-1])
            for j in cycleList:
                if j == cycle:
                    ans.append(cycle*add)
                    myDict[cycle] = cycle*add
            # print('cycle', cycle, 'add', add, cycle*add, '+++++++++++')
            # add += int(data[-1])
            for j in cycleList:
                if j == cycle:
                    ans.append(cycle*add)
    # print(ans)
    # print(myDict)
    myList = []
    for i in myDict.items():
        for j in cycleList:
            if i[0] == j:
                myList.append(i[1])
    print('part01:', sum(myList))
part01()

def part02():
    with open('day10.txt', 'rt') as myFile:
        data = myFile.read().splitlines()
    # print('#########################################')
    currentCRT = 0
    spritePos = 1
    x=''
    for i in data:
        if currentCRT > 39:
            currentCRT = 0
        data = i.split(' ')
        # print(data)
        if data[0] == 'noop':
            if currentCRT == spritePos-1 or currentCRT == spritePos or currentCRT == spritePos+1:
                x += '█'
                currentCRT+=1
                # print('noop spritePos:', spritePos)
            else: 
                x += '.'
                currentCRT+=1
                # print('sprite', spritePos)
        if data[0] == 'addx':
            for i in range(0,2):
                if currentCRT == spritePos-1 or currentCRT == spritePos or currentCRT == spritePos+1:
                    x += '█'
                    currentCRT+=1
                    # print('addx spritePos:', spritePos)
                else: 
                    x += '.'
                    currentCRT+=1
                    # print('sprite', spritePos)
            spritePos += int(data[-1])
            # print('sprite', spritePos)
    print(x, currentCRT)
part02()
