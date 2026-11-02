# To find whether sum of two elements in array is equal to target element - if yes - return the index


number = [19,6,8,34,77,541,65]
target = 14

for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i] + number[j] == target:
            print(i,j)
