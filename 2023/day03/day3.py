import re

# Day 3 part 1
sum = 0
numbers = list()
with open('day3.txt') as file:
    lines = file.readlines()
    for line_number, line in enumerate(lines):
        n = 0
        while n < len(line):
             number = re.search(r"\d+", line[n:])
             if not number:
                 break
                
             previous_line_number = max(0, line_number - 1)
             next_line_number = line_number + 2 
             start_char_index = max(0, n + number.span()[0] - 1)
             end_char_index = n + number.span()[1] + 1

             is_part_number = False
             for surrounding_line in lines[previous_line_number:next_line_number]:
                 if is_part_number:
                     break
                 for c in surrounding_line[start_char_index:end_char_index]:
                     if c != "." and c!= "\n" and not c.isnumeric(): 
                         is_part_number = True
                         sum += int(number.group())
                         break

             n += number.span()[1]
print(sum)


# Day 3 part 2
sum = 0
numbers = list()
with open('day3.txt') as file:
    lines = file.readlines()
    for line_number, line in enumerate(lines):
        possible_gear = re.finditer(r"\*", line)
        for g in possible_gear:

             previous_line_number = max(0, line_number - 1)
             next_line_number = line_number + 2 
             surrounding_numbers = list()

             for surrounding_line in lines[previous_line_number:next_line_number]:
                 numbers = re.finditer(r"\d+", surrounding_line)
                 if numbers:
                     for n in numbers:
                         if n.span()[1] >= g.span()[0] and n.span()[0] <= g.span()[1]:
                             surrounding_numbers.append(n)

             if len(surrounding_numbers) == 2:
                 power = 1
                 for value in surrounding_numbers:
                     power *= int(value.group())
                 sum += power
print(sum)
