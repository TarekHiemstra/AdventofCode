import re

# Day 4 part 1 & 2
with open('day4.txt') as file:
    lines = file.readlines()
    total_part_1 = 0
    total_part_2 = [1] * len(lines)
    
    for line_number, line in enumerate(lines):
        numbers_matching_count = 0

        winning_numbers, my_numbers = line.split("|")
        winning_numbers = re.findall(r"\d+", winning_numbers)[1:]
        my_numbers = re.findall(r"\d+", my_numbers)
        
        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                numbers_matching_count += 1

        if numbers_matching_count:
            # Part 1
            if numbers_matching_count:
                total_part_1 += 2 ** (numbers_matching_count -1)
            # Part 2
            for idx, card in enumerate(total_part_2[line_number + 1: line_number + 1 + numbers_matching_count]):
                total_part_2[line_number + 1 + idx] += 1 * total_part_2[line_number]

total_part_2 = sum(total_part_2)
print(total_part_1)
print(total_part_2)
