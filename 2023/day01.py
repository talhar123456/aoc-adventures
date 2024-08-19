with open('day01.txt', 'rt') as file:
    data = file.read().splitlines()
numbers = []
finalNumbers = []
for word in data:
    for letter in word:
        if letter.isdigit():
            numbers.append(letter)
    if len(numbers) == 1:
        result = numbers[0] + numbers[0]
        finalNumbers.append(int(result))
    else:
        result = numbers[0] + numbers[-1]
        finalNumbers.append(int(result))
    numbers.clear()
print(sum(finalNumbers))
