# Given a string, find the first character that appears exactly once.

input_string = "swiss"

non_repeating = ""

for i in range(len(input_string)):

    count = 0

    for j in range(len(input_string)):

        if input_string[i] == input_string[j]:
            count = count + 1

    if count == 1:
        non_repeating = input_string[i]
        break

if non_repeating != "":
    print("First non-repeating character:", non_repeating)
else:
    print("No non-repeating character found")




"""
We need to count how many times each character appears.
1. Select a character.
2. Initialise count = 0.
3. Compare it against every character in the string.
4. Increase count whenever they match.
5. If count equals 1, we found the first non-repeating character.
6. Stop using break.
"""
