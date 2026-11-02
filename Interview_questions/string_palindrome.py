# Given a string, check whether it reads the same forward and backward.

input_string = "madam"

reverse_string = ""

for i in range(len(input_string)):
    reverse_string = input_string[i] + reverse_string

if input_string == reverse_string:
    print("Palindrome")
else:
    print("Not palindrome")


