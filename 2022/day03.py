from collections import Counter
import string
alphabet = list(string.ascii_lowercase+string.ascii_uppercase)
duplicate = []
numbers = []
numbers2 = []
def part01():
    with open('day03.txt', 'rt') as myFile:
        data = myFile.readlines()
        data = ''.join(data).split()
    for line in data:
        length = int(len(line)/2)
        first = Counter(line[:length])
        second = Counter(line[length:])
        firstList = list(first)
        secondList = list(second)
        for i in firstList:
            for j in secondList:
                if ord(i) == ord(j):
                    duplicate.append(i)
    for i in duplicate:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                numbers.append(j+1)
    print('part01: ', sum(numbers))
part01()
def part02():
    x = []
    with open('day03.txt', 'rt') as myFile:
        data = myFile.readlines()
        data = ''.join(data).split()
    for i in range(0, len(data), 3):
        first = data[i]
        second = data[i+1]
        third = data[i+2]
        # print(first,second,third)
        first = (Counter(first).keys())
        # print(first)
        for i in first:
            if i in second and i in third:
                x.append(i)
    # print(x)
    for i in x:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                numbers2.append(j+1)
    print('part02: ', sum(numbers2))
part02()
