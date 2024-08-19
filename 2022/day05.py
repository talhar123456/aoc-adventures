import re
stacks = [
        ['R','N','F','V','L','J','S','M'], 
        ['P','N','D','Z','F','J','W','H'],
        ['W','R','C','D','G'],
        ['N','B','S'],
        ['M','Z','W','P','C','B','F','N'],
        ['P','R','M','W'],
        ['R','T','N','G','L','S','W'],
        ['Q','T','H','F','N','B','V'],
        ['L','M','H','Z','N','F']
        ]
def part01():
    # print(stacks[0])
    with open('day05.txt', 'rt') as myFile:
        data = myFile.read().splitlines()
    # print(data)
    for i in data:
        # print(i)
        # temp = []
        temp = re.findall(r'\d+', i)
        # print(temp)
        move = int(temp[0])
        frOm = int(temp[1])-1
        to = int(temp[2])-1
        # print(move, frOm, to)
        moveFrom = stacks[frOm]
        moveTo = stacks[to]
        # print(moveFrom, moveTo)

        # for part 01
        for i in range(0, move):
            # print(moveFrom, moveTo)
            moveTo.append(moveFrom[-1])
            moveFrom.pop()
            stacks[frOm] = moveFrom
            stacks[to] = moveTo

    # print(stacks)
    final = []
    for i in stacks:
        # print(i)
        stacksStrings = ''.join(i)
        final.append(stacksStrings[-1])
    final = ''.join(final)
    print('part01:', final)

part01()

def part02():
    # print(stacks[0])
    with open('day05.txt', 'rt') as myFile:
        data = myFile.read().splitlines()
    # print(data)
    for i in data:
        # print(i)
        # temp = []
        temp = re.findall(r'\d+', i)
        # print(temp)
        move = int(temp[0])
        frOm = int(temp[1])-1
        to = int(temp[2])-1
        # print(move, frOm, to)
        moveFrom = stacks[frOm]
        moveTo = stacks[to]
        # print(moveFrom, moveTo)

        # for part02
        temp = moveFrom[-move:]
        del moveFrom[-move:]
        for i in temp:
            moveTo.append(i)
        stacks[frOm] = moveFrom
        stacks[to] = moveTo
        
    # print(stacks)
    final = []
    for i in stacks:
        # print(i)
        stacksStrings = ''.join(i)
        final.append(stacksStrings[-1])
    final = ''.join(final)
    print('part02:', final)

part02()