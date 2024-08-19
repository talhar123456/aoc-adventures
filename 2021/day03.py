with open('day03.txt', 'rt') as file:
    data = file.read().splitlines()
length = len(data[0])
final = []
for j in range(length):
    List = []
    # print('***')
    for i in data:
        List.append(int(i[j]))
    if List.count(0) < List.count(1):
        final.append('1')
    elif List.count(1) < List.count(0):
        final.append('0')
# print(final)
final2 = final
final = ''.join(final)
gamma = int(final, 2)
for i in range(len(final2)):
    if final2[i] == '0':
        final2[i] = '1'
    else:
        final2[i] = '0'
# print(final2)
final2 = ''.join(final2)
epsilon = int(final2, 2)
print('part 01: ', gamma * epsilon)
#####################################################
# PART 2

data2 = []
for i in data:
    data2.append(i)

# processing for OXYGEN RATE
length = len(data[0])
for j in range(length):
    List = []
    todelete = []
    # print('***')
    for i in data:
        List.append(int(i[j]))
    # print(List, '***')
    # oxygen rating
    if len(List) == 1:
        break
    else:
        if List.count(0) < List.count(1):
            for k in range(len(List)):
                if List[k] == 0:
                    todelete.append(k)
        elif List.count(1) < List.count(0):
            for k in range(len(List)):
                if List[k] == 1:
                    todelete.append(k)
        elif List.count(1) == List.count(0):
            for k in range(len(List)):
                if List[k] == 0:
                    todelete.append(k)
    # print(todelete)
    for x in reversed(todelete):
        data.pop(x)
# print('data1: ', data)
a = int(data[0], 2)
# print(a)

# processing for CARBON RATE
length = len(data2[0])
for j in range(length):
    List = []
    todelete = []
    # print('***')
    for i in data2:
        List.append(int(i[j]))
    # print(List, '***')
    # carbon rating
    if len(List) == 1:
        break
    else:
        if List.count(0) < List.count(1):
            for k in range(len(List)):
                if List[k] == 1:
                    todelete.append(k)
        elif List.count(1) < List.count(0):
            for k in range(len(List)):
                if List[k] == 0:
                    todelete.append(k)
        elif List.count(1) == List.count(0):
            for k in range(len(List)):
                if List[k] == 1:
                    todelete.append(k)
    # print(todelete)
    for x in reversed(todelete):
        data2.pop(x)
# print('data2: ', data2)
b = int(data2[0], 2)
# print(b)
print('part 02: ', a * b)
