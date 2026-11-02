# Given an array of integers and a target difference, find two numbers whose absolute difference equals the target.

numbers = [5, 20, 3, 2, 50, 80]
target = 78

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] - numbers[j] == target:
            print(numbers[i], numbers[j])

        elif numbers[j] - numbers[i] == target:
            print(numbers[i], numbers[j])