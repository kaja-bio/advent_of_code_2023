total = 0
with open("practice.txt", "r") as f:
    for line in f:
        array = []
        for element in line:
            if element.isdigit():
                array.append(element)
        if len(array) == 1:
            sum = array[0] + array[0]
            total += int(sum)
        elif len(array) > 1:
            sum = array[0] + array[-1]
            total += int(sum)


print(f"The sum is {total}")
