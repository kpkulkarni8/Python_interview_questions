# Given two arrays, find all elements that are present in both arrays. Print each common element only once.

array1 = [10, 20, 20, 30, 40]
array2 = [20, 20, 40, 50]

for i in range(len(array1)):

    already_checked = False

    for k in range(i):
        if array1[i] == array1[k]:
            already_checked = True
            break

    if not already_checked:

        for j in range(len(array2)):
            if array1[i] == array2[j]:
                print(array1[i])
                break


'''
There are three loops/operations involved:
Operation	Purpose
Outer loop (i)	Select an element from array1
Previous-element loop (k)	Prevent duplicate output
Inner loop (j)	Search for the element in array2

The break inside the inner loop ensures that once a match is found, we don't continue searching for the same element in array2.

'''