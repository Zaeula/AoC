import re

file = "data.txt"
with open(file) as f:
    content = f.readlines()

where_symbols = ['#', '*', '@', '$', '+', '&', '%', '/', '-', '=']
where_symbolsp2 = ['*']
numbers = {}
numbers_pos = []
symbol_count = 0
ttl_sum = 0

for line_index, line in enumerate(content):
    for char_index, char in enumerate(line):
        if char in where_symbols:
            for i, j in [(-1, -1), (1, -1), (-1, 1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= line_index + i < len(content) and 0 <= char_index + j < len(line):
                    if content[line_index + i][char_index + j].isdigit():
                        left = char_index + j
                        while left > 0 and content[line_index + i][left - 1].isdigit():
                            left -= 1
                        right = char_index + j
                        while right < len(line) - 1 and content[line_index + i][right + 1].isdigit():
                            right += 1
                        full_number = content[line_index + i][left:right+1]
                        position = (line_index + i, left)

                        if (full_number, position) not in numbers_pos:
                            numbers_pos.append((full_number, position))
                            symbol_count += 1

                            if (line_index, char_index) in numbers:
                                numbers[(line_index, char_index)].append(int(full_number))
                            else:
                                numbers[(line_index, char_index)] = [int(full_number)]

            if symbol_count < 2:
                remove = numbers_pos.pop()
            symbol_count = 0

for symbol, nums in numbers.items():
    if len(nums) == 2:
        product = nums[0] * nums[1]
        ttl_sum += product

print(ttl_sum)


# print(sum(numbers))
