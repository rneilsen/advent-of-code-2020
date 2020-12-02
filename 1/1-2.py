TARGET = 2020

# Read file and sort
with open('input') as f:
    numbers = [int(n) for n in f.read().splitlines()]

numbers.sort()

# set k to end of list, i and j to ends of section before k'th element
(i, j, k) = (0, len(numbers) - 2, len(numbers) - 1)

while True:
    target = TARGET - numbers[k]

    if i == j:
        # k'th value is no good, pull k back 1 and try again
        k -= 1
        (i, j) = (0, k-1)
        continue
    elif numbers[i] + numbers[j] > target:
        # sum is too high, pull j back 1
        j -= 1
    elif numbers[i] + numbers[j] < target:
        # sum is too low, push i up 1
        i += 1
    else:
        # target found!
        print(numbers[i], numbers[j], numbers[k], numbers[i] * numbers[j] * numbers[k])
        exit()
