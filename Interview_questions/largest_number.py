# find the largest number in the array

numbers=[10,67,66,89,100,87,1]

# lets assume first number as larget
largest=numbers[0]


for i in range(len(numbers)):
    if numbers[i]>largest:
        largest=numbers[i]
print(largest)