import re

file = "data.txt"
with open(file) as f:
    content = f.readlines()

game_id_counter = 0 #for part 1
ttl_power = 0 #for part 2

maxRed = 12
maxGreen = 13
maxBlue = 14

for i in range(len(content)):
    content[i] = content[i].split(':')

ok_games = 0
game_counts = []

for i in range(len(content)):
    line = content[i][1]
    max_counts = {"red": 0, "green": 0, "blue": 0}
    red = re.findall(r'(\d+)\s*red', line)
    green = re.findall(r'(\d+)\s*green', line)
    blue = re.findall(r'(\d+)\s*blue', line)
    #print(red, green, blue)
    
    red = max(int(num) for num in red)
    green = max(int(num) for num in green)
    blue = max(int(num) for num in blue)
    print(red, green, blue)

    power = int(red) * int(green) * int(blue)

    print(power)

    ttl_power += power


    #for part 1
    # if int(red) <= maxRed and int(green) <= maxGreen and int(blue) <= maxBlue:
    #     ok_games += 1
    #     print("game", i+1, "is ok")
    #     game_id_counter += i+1
    #     print(game_id_counter)
    # else:
    #     print("game", i+1, "is not ok")
    #     print(game_id_counter)

print(ttl_power)
# print(ok_games)
# print(game_id_counter)

#print(game_counts)
    


# print(content)