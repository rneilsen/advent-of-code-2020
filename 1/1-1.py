TARGET = 2020

with open('input') as f:
    numbers = [int(n) for n in f.read().splitlines()]

numbers.sort()

(i, j) = (0, len(numbers) - 1)

while True:
    if numbers[i] + numbers[j] > TARGET:
        j -= 1
    elif numbers[i] + numbers[j] < TARGET:
        i += 1
    else:
        print(numbers[i], numbers[j], numbers[i] * numbers[j])
        exit()
