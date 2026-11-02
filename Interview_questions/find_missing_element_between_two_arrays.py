# You are given two arrays. Find the elements present in the first array but missing from the second array.

array1 = [10, 20, 30, 40, 50, 60]
array2 = [20, 40, 60]

for i in range(len(array1)):

    found = False

    for j in range(len(array2)):

        if array1[i] == array2[j]:
            found = True
            break

    if found == False:
        print(array1[i])