x = open("day1_input1.txt", "r")

data = x.read()
data_list = data.split("\n")

prev = 50
current_point = 50
zeroes = 0

for move in data_list:
    prev = current_point
    number = int(move[1:])
    if move[0] == "R":
        current_point = (current_point + number)

    elif move[0] == "L":
        current_point = (current_point - number)
    else:
        print("Fail")

    if (current_point < 0 and prev != 0) or current_point == 0:
        zeroes += 1
    if abs(current_point) >= 100:
        zeroes += abs(current_point) // 100

    current_point = current_point % 100

print(zeroes)
