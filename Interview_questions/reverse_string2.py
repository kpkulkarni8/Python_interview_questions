# reverse string without using in built functions
#

input_string = "Python Programming"
reversed_string = ""

for i in range(len(input_string)):
     reversed_string=reversed_string+input_string[len(input_string) - i - 1]


print(reversed_string)