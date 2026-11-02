# find the second largest number in an array

numbers = [10,65,99,65,888,564]

first_largest=numbers[0] # strores the largest number found
second_larget=numbers[0] # stores the second larget number


for i in range(1, len(numbers)):

    if numbers[i] > first_largest:
        second_largest = first_largest
        first_largest = numbers[i]

    elif numbers[i] > second_largest and numbers[i] < first_largest:
        second_largest = numbers[i]

print("Largest:", first_largest)
print("Second largest:", second_largest)


'''

The logic:
1. If the current number is greater than first_largest:
   - Move first_largest into second_largest.
   - Update first_largest.
2. Otherwise, if the current number is smaller than first_largest but greater than second_largest:
   - Update second_largest.
   
   '''