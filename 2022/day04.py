from collections import Counter
def part01():
    with open('day04.txt', 'rt') as myFile:
        data = myFile.read().split()
        data = ' '.join(data)
        data = data.split(' ')
        data = ' '.join(data)
        data = data.split(' ')
    temp = []
    count = 0
    count2 = 0
    for i in data:
        temp.append(i.split(','))
    for i in temp:
        firstRange = i[0]
        secondRange = i[1]
        firstRange = firstRange.replace('-', ' ')
        secondRange = secondRange.replace('-', ' ')
        firstRange = firstRange.split(' ')
        secondRange = secondRange.split(' ')
        val1 = int(firstRange[0])
        val2 = int(firstRange[1])
        val3 = int(secondRange[0])
        val4 = int(secondRange[1])
        firstRangeList = []
        secondRangeList = []
        for i in range(val1, val2+1):
            firstRangeList.append(i)
        for i in range(val3, val4+1):
            secondRangeList.append(i)
        if(all(x in firstRangeList for x in secondRangeList)):
            count += 1
        elif(all(x in secondRangeList for x in firstRangeList)):
            count += 1
        # print('***********')
        # print(firstRangeList, secondRangeList)
        for i in secondRangeList:
            firstRangeList.append(i)
        CombinedList = (Counter(firstRangeList))
        if sum(CombinedList.values()) > len(CombinedList.values()):
            count2+=1
    print('part01:', count,'part02:', count2)
part01()