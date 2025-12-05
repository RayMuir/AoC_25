x = open("day5_input.txt", "r")

data = x.read()
ranges = data.split("\n")

x = open("day5_input2.txt", "r")

data1 = x.read()
ids = data1.split("\n")

ids = list(map(int, ids))
ranges = [tuple(map(int, item.split('-'))) for item in ranges]

total = 0
for id in ids:
    for (start, stop) in ranges:
        if id >= start and id <= int(stop):
            total += 1
            break
print(total)
