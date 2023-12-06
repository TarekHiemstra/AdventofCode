import re

# Day 2 part 1
sum = 0
with open('day2.txt') as file:
    limits = {"red": 12, "green": 13, "blue": 14}
    lines = file.readlines()
    for idx, line in enumerate(lines):
        numbers = re.findall(r'(\d+) (\w+)', line)
        possible = True
        for number, color in numbers:
            if int(number) > limits.get(color):
                possible = False
                break
        if possible:
            sum += idx + 1
    print(sum)     

# Day 2 part 2
sum = 0
with open('day2.txt') as file:
    lines = file.readlines()
    for idx, line in enumerate(lines):
        limits = {"red": [], "green": [], "blue": []}
        maximums = list()
        numbers = re.findall(r'(\d+) (\w+)', line)
        for number, color in numbers:
            limits.get(color).append(number)
        for key, value in limits.items():
            maximums.append(max(list(map(int, value))))
        power = 1
        for value in maximums:
            power *= value   
        sum += power
    print(sum)
