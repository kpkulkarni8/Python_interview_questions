# given a string reverse it without using in built functions


input_string = "python"

reversed_string = " "

for i in range(len(input_string)):
    reversed_string = input_string[i] + reversed_string
    print(reversed_string)


