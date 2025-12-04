x = open("day3_input.txt", "r")

data = x.read()
data_list = data.split("\n")

first_highest = 0

second_highest = 0
total = 0

for bank in data_list:
    bank_str = str(bank)
    for number in bank_str:
        num = int(number)
        if num >= first_highest:
            if num >= second_highest:
                if second_highest >= first_highest:
                    first_highest = second_highest
            else:
                first_highest = second_highest
            second_highest = num
        else:
            if second_highest > first_highest:
                first_highest = second_highest
                second_highest = num
            if num >= second_highest:
                second_highest = num
    n = str(first_highest) + str(second_highest)
    total += int(n)
    first_highest = 0
    second_highest = 0
print(total)

            
 


