#Given a string, find the first character that appears more than once.

input_string = "programming"

found = False

for i in range(len(input_string)):

    for j in range(i + 1, len(input_string)):

        if input_string[i] == input_string[j]:
            print("First repeated character:", input_string[i])
            found = True
            break

    if found:
        break

if not found:
    print("No repeated character found")