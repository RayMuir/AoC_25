x = open("day2_input.txt", "r")

data = x.read()
data_list = data.split(",")

new_list = []
for x in data_list:
    y = x.split("-")
    new_list.extend(y)

total = 0

# new_list = [11, 22, 95, 115, 998, 1012, 1188511880, 1188511890, 222220, 222224, 1698522, 1698528, 446443, 446449, 38593856, 38593862]

y = len(new_list)
if y % 2 == 0:
    y = y // 2
else:
    y = (y // 2) + 1

# For every pair of numbers in the data
for _ in range(y):
    smaller = int(new_list.pop(0))
    bigger = int(new_list.pop(0))

    amt = (bigger - smaller) + 1
    # For each number in the range of the pairs.
    for n in range(amt):
        number = smaller + n
        current = str(number)