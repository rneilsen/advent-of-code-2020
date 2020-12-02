TARGET = 2020

with open('input') as f:
    numbers = [int(n) for n in f.read().splitlines()]

numbers.sort()

(i, j, k) = (0, len(numbers) - 2, len(numbers) - 1)

while True:
    target = TARGET - numbers[k]
    if i == j:
        k -= 1
        (i, j) = 0, k-1
        continue
    elif numbers[i] + numbers[j] > target:
        j -= 1
    elif numbers[i] + numbers[j] < target:
        i += 1
    else:
        print(numbers[i], numbers[j], numbers[k], numbers[i] * numbers[j] * numbers[k])
        exit()
