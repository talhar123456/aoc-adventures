def day02():
    with open('day02.txt', 'rt') as myFile:
        data = myFile.read().splitlines()
    score1 = []
    score2 = []
    for i in data:
        if i == 'A X':
            score1.append(4)
            score2.append(3)
        if i == 'A Y':
            score1.append(8)
            score2.append(4)
        if i == 'A Z':
            score1.append(3)
            score2.append(8)
        if i == 'B X':
            score1.append(1)
            score2.append(1)
        if i == 'B Y':
            score1.append(5)
            score2.append(5)
        if i == 'B Z':
            score1.append(9)
            score2.append(9)
        if i == 'C X':
            score1.append(7)
            score2.append(2)
        if i == 'C Y':
            score1.append(2)
            score2.append(6)
        if i == 'C Z':
            score1.append(6)
            score2.append(7)
    print('part01: ', sum(score1)); print('part02: ', sum(score2))
day02()