with open('day01.txt', 'rt') as file:
    data = file.read().splitlines()
count = 0
x = 0
for i in data:
    if x < int(i):
        count += 1
    x = int(i)
print('part 01: ', count-1)
count = 0
x = 0
combined = data+data
for i in range(len(data)):
    sum = int(combined[i]) + int(combined[i+1]) + int(combined[i+2])
    if x < sum:
        count += 1
    x = sum
print('part 02: ', count-1)
