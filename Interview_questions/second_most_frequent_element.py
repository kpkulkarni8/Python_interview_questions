# Given an array of integers, find the element with the second-highest frequency.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]

highest_frequency = 0
second_highest_frequency = 0

most_frequent = -1
second_most_frequent = -1

for i in range(len(numbers)):

    already_checked = False

    # Check whether this number was already processed
    for k in range(i):
        if numbers[i] == numbers[k]:
            already_checked = True
            break

    if not already_checked:

        count = 0

        # Calculate frequency
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                count = count + 1

        # Find highest and second-highest frequencies
        if count > highest_frequency:

            second_highest_frequency = highest_frequency
            second_most_frequent = most_frequent

            highest_frequency = count
            most_frequent = numbers[i]

        elif count > second_highest_frequency:

            second_highest_frequency = count
            second_most_frequent = numbers[i]


if second_most_frequent != -1:
    print("Most frequent element:", most_frequent)
    print("Highest frequency:", highest_frequency)

    print("Second most frequent element:", second_most_frequent)
    print("Second highest frequency:", second_highest_frequency)

else:
    print("No second most frequent element")