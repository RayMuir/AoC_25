x = open("day4_input.txt", "r")


data = x.read()
data_list = data.split("\n")
new = [list(line) for line in data_list]

total = 0


for y in range(len(new)):
    for x in range(len(new[y])):
        if new[y][x]!= '.':
            count = 0
            for y_moving in [-1, 0, 1]:
                for x_moving in [-1, 0, 1]:
                    if ((x_moving == 0) and (y_moving == 0)):
                        continue
                    if y + y_moving >= 0 and y + y_moving < ((len(new))) and x + x_moving >= 0 and x + x_moving < len(new[x]):
                        j = new[y + y_moving][x + x_moving]
                        if new[y + y_moving][x + x_moving] == '@':
                            count += 1
            if count < 4:
                total += 1
            count = 0
print(total)

