number = [1, 2, 4, 5, 6]

actual_sum = 0
expected_sum = 0

# Calculate actual sum
for i in range(len(number)):
    actual_sum = actual_sum + number[i]

# Calculate expected sum
for i in range(1, len(number) + 2):
    expected_sum = expected_sum + i

missing_number = expected_sum - actual_sum

print("Missing number:", missing_number)


'''

Why len(number) + 2?
- Array length is 5.
- There should be 6 numbers.
- range(1, 7) generates 1 through 6 because the ending value is excluded.

we can also do it by n(n+1)/2


'''