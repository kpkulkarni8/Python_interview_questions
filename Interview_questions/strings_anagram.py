# Given two strings, determine whether they contain the same characters with the same frequency, but possibly in a different order.

string1 = "listen"
string2 = "silent"

if len(string1) != len(string2):
    print("Not Anagrams")

else:
    is_anagram = True

    for i in range(len(string1)):

        count1 = 0
        count2 = 0

        for j in range(len(string1)):
            if string1[i] == string1[j]:
                count1 = count1 + 1

        for k in range(len(string2)):
            if string1[i] == string2[k]:
                count2 = count2 + 1

        if count1 != count2:
            is_anagram = False
            break

    if is_anagram:
        print("Anagrams")
    else:
        print("Not Anagrams")
