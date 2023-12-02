

file = "data.txt"
with open(file) as f:
    content = f.readlines()

#added for part 2

# help_dict = {
#     'oneight': '18',
#     'twone': '21',
#     'eightwo': '82',
#     'threeight': '38',
#     'fiveeight': '58',
#     'sevenine': '79',
#     'eighthree': '83',
#     'nineight': '98',
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9',
#     'zero': '0',
# }

# for i in range(len(content)):
#     for key in help_dict:
#         content[i] = content[i].replace(key, help_dict[key])


#part 1

content = [''.join(ch for ch in x if ch.isdigit()) for x in content]

for i in range(len(content)):
    content[i] = int(content[i])
    str_content = str(content[i])
    content[i] = (int(str_content[0]), int(str_content[-1]))
    print(content[i])


for i in range(len(content)):
    content[i] = (str(content[i][0]) + str(content[i][1]))
    content[i] = int(content[i])
answer = sum(content)

print("my answer to this nice question is", + answer)