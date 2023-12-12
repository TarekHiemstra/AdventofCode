# Day 1 part 1
total = 0
with open('day1.txt') as file:
    lines = file.readlines()
    for line in lines:
        my_list = list()
        for c in line:
            if c.isnumeric():
                my_list.append(c)
        line_value = str(my_list[0]) + str(my_list[-1])
        total += int(line_value)
print(total)


# Day 1 part 2
total = 0
with open('day1.txt') as file:
    lines = file.readlines()
    for line in lines:
        numbers = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, 
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9
        }
        
        lowest_index = len(line)
        highest_index = 0
        first_number = len(line)
        last_number = 0
        
        for number in numbers:
            if number in line:
                first_occurence = line.find(number)
                last_occurence = line.rfind(number)
                if first_occurence <= lowest_index:
                    lowest_index = first_occurence
                    first_number = numbers.get(number)
                if last_occurence >= highest_index:
                    highest_index = last_occurence
                    last_number = numbers.get(number)
        line_value = str(first_number) + str(last_number)
        total += int(line_value)
print(total)
