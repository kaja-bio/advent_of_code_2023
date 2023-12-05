import regex as re

with open("./day_two/cubes.txt", "r") as f:
    total = 0
    for line in f:
        green = re.findall(r'\d+\s+green', line)
        green_num = []
        for x in green:
            digits = ''.join(c for c in x if c.isdigit())
            for subitem in x.split():
                if digits:
                    green_num.append(int(digits))
        max_green = max(green_num)
        blue = re.findall(r'\d+\s+blue', line)
        blue_num = []
        for z in blue:
            digits = ''.join(c for c in z if c.isdigit())
            for subitemb in z.split():
                if digits:
                    blue_num.append(int(digits))
        max_blue = max(blue_num)
        red = re.findall(r'\d+\s+red', line)
        red_num = []
        for y in red:
            digits = ''.join(c for c in y if c.isdigit())
            for subitemc in y.split():
                if digits:
                    red_num.append(int(digits))
        max_red = max(red_num)
        power = max_red * max_blue * max_green
        print(power)
        total += power

print(f"The total is {total}")
