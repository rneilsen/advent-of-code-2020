TARGET = 2020

# Read input file and sort
with open('input') as f:
    numbers = [int(n) for n in f.read().splitlines()]

numbers.sort()

# set i, j to ends of the list
(i, j) = (0, len(numbers) - 1)

while True:
    if numbers[i] + numbers[j] > TARGET:
        # sum is too high, pull j back 1
        j -= 1
    elif numbers[i] + numbers[j] < TARGET:
        # sum is too low, push i up 1
        i += 1
    else:
        # target found!
        print(numbers[i], numbers[j], numbers[i] * numbers[j])
        exit()
