def part01():
    with open('day08.txt', 'rt') as myFile:
        data = myFile.read().splitlines()
    # print(data)
    trees=[]
    for i in data:
        trees.append(list(i))
    # print(trees, '********')
    x = (len(trees)-2)*2
    first = trees[0]
    last = trees[-1]
    total = 0
    y = len(first)+len(last)
    for i in range(1, len(trees)-1):
        for j in range(1, len(trees)-1):
            currentTree = int(trees[i][j])    
            # print('current tree', currentTree)
            left = trees[i][:j]
            right = trees[i][j+1:] 
            bottom = [trees[i+k][j] for k in range(1, len(trees)-i)]
            up = [trees[i-k][j] for k in range(1, i+1)]
            # not working:
            # for k in range(1, len(trees)-i, trees[i+k]):
            #     bottom = [trees[k][j]]
            # print('bottom', bottom, 'up', up)
            # print('left', left, 'right', right)
            left = ([int (x) for x in left])
            right = ([int (x) for x in right])
            bottom = ([int (x) for x in bottom])
            up = ([int (x) for x in up])
            if max(left)<currentTree or max(right)<currentTree or max(up)<currentTree or max(bottom)<currentTree:
                total += 1
    print(x + y + total)
part01()

def part02():
    with open('day08.txt', 'rt') as myFile:
        data = myFile.read().splitlines()
    # print(data)
    trees=[]
    for i in data:
        trees.append(list(i))
    # for i in trees:
    #     print(i)
    # print(trees, '********')
    # x = (len(trees)-2)*2
    first = trees[0]
    last = trees[-1]
    total = []
    # y = len(first)+len(last)
    for i in range(1, len(trees)-1):
        for j in range(1, len(trees)-1):
            currentTree = int(trees[i][j])    
            # print('current tree', currentTree)
            left = trees[i][:j]
            right = trees[i][j+1:] 
            bottom = [trees[i+k][j] for k in range(1, len(trees)-i)]
            up = [trees[i-k][j] for k in range(1, i+1)]
            left = ([int (x) for x in left])
            right = ([int (x) for x in right])
            bottom = ([int (x) for x in bottom])
            up = ([int (x) for x in up])
            # print(currentTree, 'left', left, 'right', right, 'bottom', bottom, 'up', up)
            countLeft = 0
            countRight = 0
            countBottom = 0
            countUp = 0
            for l in reversed(left):
                if l < currentTree:
                    countLeft+=1
                elif l >= currentTree:
                    countLeft+=1
                    break
            for l in right:
                if l < currentTree:
                    countRight+=1
                elif l >= currentTree:
                    countRight+=1
                    break
            for l in bottom:
                if l < currentTree:
                    countBottom+=1
                elif l >= currentTree:
                    countBottom+=1
                    break
            for l in up:
                if l < currentTree:
                    countUp+=1
                elif l >= currentTree:
                    countUp+=1
                    break
            # print(countLeft,'countLeft')
            # print(countRight,'countRight')
            # print(countBottom,'countBottom')
            # print(countUp,'countUp')
            total.append(countBottom*countLeft*countUp*countRight)
    print(max(total))
part02()
