# Given an array of integers, count how many times each number appears.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]

for i in range(len(numbers)):

    count = 0

    for j in range(len(numbers)):

        if numbers[i] == numbers[j]:
            count = count + 1

    print(numbers[i], "appears", count, "times")