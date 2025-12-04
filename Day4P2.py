x = open("day4_input.txt", "r")

data = x.read()
data_list = data.split("\n")
new = [list(line) for line in data_list]

total = 0

total_total = 0

new_new = [['.' for _ in range(len(new[0]))] for _ in range(len(new))]

while True:
    total = 0
    for y in range(len(new)):
        for x in range(len(new[y])):
            new_new[y][x] = new[y][x]
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
                    new_new[y][x] = '.'
            count = 0
    if total == 0: 
        break
    new = new_new
    new_new = [['.' for _ in range(len(new[0]))] for _ in range(len(new))]
    total_total += total
print(total_total)
