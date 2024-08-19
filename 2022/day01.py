def day01():
    with open('day01.txt', 'rt') as myFile:
        data = myFile.read()
    dataList = data.splitlines()
    count = 0
    integers = []
    for i in dataList:
        if i != '':
            count += int(i)
        elif i == '':
            integers.append(count)
            count = 0
    integers.append(count)
    print('part01: ', max(integers))
    sortedVal = sorted(integers)
    reverse = sortedVal.reverse()
    print('part02: ', sum(sortedVal[:3]))
day01()
