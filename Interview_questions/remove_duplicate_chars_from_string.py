# Given a string, remove duplicate characters while preserving the original order.

input_string = "programming"
output_string = ""

for i in range(len(input_string)):

    already_exists = False

    for j in range(len(output_string)):

        if input_string[i] == output_string[j]:
            already_exists = True
            break

    if not already_exists:
        output_string = output_string + input_string[i]

print(output_string)