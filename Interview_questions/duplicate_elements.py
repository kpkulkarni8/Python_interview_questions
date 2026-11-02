# Given an array of integers, identify all elements that appear more than once.

numbers = [10, 20, 20, 20, 30]

for i in range(len(numbers)):

    already_counted = False

    for k in range(i):
        if numbers[i] == numbers[k]:
            already_counted = True
            break

    if not already_counted:

        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                print(numbers[i])
                break

