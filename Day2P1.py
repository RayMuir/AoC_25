x = open("day2_input.txt", "r")

data = x.read()
data_list = data.split(",")

new_list = []
for x in data_list:
    y = x.split("-")
    new_list.extend(y)

total = 0

# new_list = [11, 22, 95, 115, 998, 1012, 1188511880, 1188511890, 222220, 222224, 1698522, 1698528, 446443, 446449, 38593856, 38593862]

y = (len(new_list) + 1) // 2
for _ in range(y):
    smaller = int(new_list.pop(0))
    bigger = int(new_list.pop(0))

    for number in range(smaller, bigger + 1):
        current = str(number)
        if len(current) % 2 == 0:
            fst_half = current[ : (len(current) // 2)]
            snd_half = current[(len(current) // 2) : ]
            if fst_half == snd_half:
                total += number

print(total)


# y = (len(new_list) + 1) // 2

# for smaller, bigger in zip(new_list[::2], new_list[1::2]):
#     smaller = int(smaller)
#     bigger = int(bigger)

#     for number in range(smaller, bigger + 1):
#         current = str(number)
#         if len(current) % 2 == 0:
#             fst_half = current[ : (len(current) // 2)]
#             snd_half = current[(len(current) // 2) : ]
#             if fst_half == snd_half:
#                 total += number

# print(total)
