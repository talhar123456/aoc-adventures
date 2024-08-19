from collections import Counter
def part01():
    with open('day06.txt', 'rt') as myFile:
            data = myFile.read()
    # print(data)
    for i in range(1, len(data)-1):
        temp = data[i]+data[i+1]+data[i+2]+data[i+3]
        # print(temp, Counter(temp), len(Counter(temp)))
        if len(Counter(temp)) == 4:
            print('part01:' ,data.index(temp)+4)
            break
    for i in range(1, len(data)-1):
        temp2 = data[i:i+14]
        # print(temp, Counter(temp), len(Counter(temp)))
        if len(Counter(temp2)) == 14:
            print('part02:' ,data.index(temp2)+14)
            break
part01()