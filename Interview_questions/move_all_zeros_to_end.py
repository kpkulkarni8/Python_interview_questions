# Given an array, move all zeros to the end while maintaining the relative order of non-zero elements.

numbers = [0, 1, 0, 3, 12, 0, 5]

position = 0

# Move all non-zero elements to the beginning
for i in range(len(numbers)):

    if numbers[i] != 0:
        numbers[position] = numbers[i]
        position = position + 1

# Fill remaining positions with zeros
for i in range(position, len(numbers)):
    numbers[i] = 0

print(numbers)


'''
Logic:
1. Start position at 0.
2. Traverse the array.
3. Whenever you find a non-zero element, place it at position.
4. Increment position.
5. After all non-zero elements have been moved, fill the remaining positions with zeros.
'''