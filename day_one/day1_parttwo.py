import regex as re
total = 0
with open("day_1.txt", "r") as f:
    for line in f:
        match = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|[1-9])', line, overlapped=True)
        for i in range(len(match)):
            if match[i] == "one":
                match[i] = "1"
            elif match[i] == "two":
                match[i] = "2"
            elif match[i] == "three":
                match[i] = "3"
            elif match[i] == "four":
                match[i] = "4"
            elif match[i] == "five":
                match[i] = "5"
            elif match[i] == "six":
                match[i] = "6"
            elif match[i] == "seven":
                match[i] = "7"
            elif match[i] == "eight":
                match[i] = "8"
            elif match[i] == "nine":
                match[i] = "9"                
        if len(match) == 1:
            concat = match[0] + match[0]
            total += int(concat)
        if len(match) > 1:
            concat = match[0] + match[-1]
            total += int(concat)
print(f"The sum is {total}")