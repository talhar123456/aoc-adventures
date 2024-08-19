with open('day02.txt', 'rt') as file:
    data = file.read().splitlines()
depth = 0
horPos = 0
for i in data:
    i = i.split(' ')
    pos = i[0]
    val = int(i[1])
    if pos == 'forward':
        horPos += val
    elif pos == 'up':
        depth -= val
    elif pos == 'down':
        depth += val
print('part 01: ', depth*horPos)

depth = 0
horPos = 0
aim = 0
depthList = []
for i in data:
    i = i.split(' ')
    pos = i[0]
    val = int(i[1])
    if pos == 'forward':
        horPos += val
        depth = aim * val
        depthList.append(depth)
    elif pos == 'up':
        depth -= val
        aim -= val
    elif pos == 'down':
        depth += val
        aim += val
print('part 02: ', sum(depthList) * horPos)
