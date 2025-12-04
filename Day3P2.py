x = open("day3_input.txt", "r")

data = x.read()
data_list = data.split("\n")

total = 0
tot = []
highest = 0
index = 0

for bank in data_list:
    bank_str = str(bank)
    boundary = 11
    current_number = bank_str[:-boundary]
    i = 0
    for _ in bank_str:
        if len(tot) < 12:
            current_index = 0
            for n in current_number:
                i += 1
                if int(n) > highest:
                    highest = int(n)
                    current_index = i
            index = index + current_index    
            boundary = boundary - 1
            if boundary == 0:
                current_number = bank_str[index:]
            else:
                current_number = bank_str[index:-boundary]
            i = 0
            if highest != 0:
                tot.append(str(highest))
            highest = 0
    total += int(''.join(tot))
    tot = []
    index = 0
print(total)