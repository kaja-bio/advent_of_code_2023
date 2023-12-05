
import regex as re

with open("./day_two/cubes.txt", "r") as f:
    total = 0
    possible_games = []

    for line in f:
        thingy = line.split(":")
        nums = re.findall(r'\d+', thingy[0])
        id = int(nums[0])
        cubez = thingy[1].split(";")
        is_possible = True
        cube_counts = {'red': 12, 'green': 13, 'blue': 14}
        for str in cubez:
            str = str.strip()
            cubes = re.findall(r'\d+ \w+', str)
            for cube in cubes:
                count, color = cube.split()
                count = int(count)
                if cube_counts.get(color, 0) < count:
                    is_possible = False
                    break
        if is_possible:
            possible_games.append(id)

    print(f"The possible games are: {possible_games}")
    print(f"The sum of IDs of possible games is: {sum(possible_games)}")

