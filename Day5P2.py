x = open("day5_input.txt", "r")

data = x.read()
ranges = data.split("\n")

ranges = [tuple(map(int, item.split('-'))) for item in ranges]

ranges.sort(key=lambda x:x[0])
total_list = []
current_range = ranges[0]

total = 0
for i in range(len(ranges)):
    (lower, upper) = ranges[i]
    if lower > current_range[1]:
        total_list.append(current_range)
        current_range = ranges[i]
        continue
    if upper >= current_range[1]:
        current_range = (current_range[0], upper)

total_list.append(current_range)
for (x, y) in total_list:
    total += (y - x) + 1

print(total)
    