x = open("day2_input.txt", "r")

data = x.read()
data_list = data.split(",")

new_list = []
for x in data_list:
    y = x.split("-")
    new_list.extend(y)

total = 0

# new_list = [11, 22, 95, 115, 998, 1012, 1188511880, 1188511890, 222220, 222224, 1698522, 1698528, 446443, 446449, 38593856, 38593862, 565653, 565659, 824824821, 824824827, 2121212118, 2121212124]

y = (len(new_list) + 1) // 2 # ceiling div

# For every pair of numbers in the data
for _ in range(y):
    smaller = int(new_list.pop(0))
    bigger = int(new_list.pop(0))

    # For each number in the range of the pairs.
    for number in range(smaller, bigger + 1):
        current = str(number)
 
        # we want to check up to half way for patterns
        up_to_multiple = len(current) // 2
        
        for n in range(1, up_to_multiple + 1):
            # is n a multiple of the current number
            if len(current) % n == 0: 
                pattern = current[:n]
                multiplier = len(current) // n
                test = pattern * multiplier
                if test == current:
                    total += number
                    break
print(total)