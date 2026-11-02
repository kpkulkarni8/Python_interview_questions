# Given an array of integers, find the maximum sum of two consecutive elements.

numbers = [4, 2, 10, 8, 1, 9]

max_sum = numbers[0] + numbers[1]

for i in range(len(numbers) - 1):

    current_sum = numbers[i] + numbers[i + 1]

    if current_sum > max_sum:
        max_sum = current_sum

print("Maximum consecutive sum:", max_sum)