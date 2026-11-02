# Given an array of integers, find both the largest and smallest numbers without using built-in functions.


numbers = [45, 12, 89, 3, 67, 100, 8]

largest = numbers[0]
smallest = numbers[0]

for i in range(1, len(numbers)):

    if numbers[i] > largest:
        largest = numbers[i]

    if numbers[i] < smallest:
        smallest = numbers[i]

print("Largest:", largest)
print("Smallest:", smallest)