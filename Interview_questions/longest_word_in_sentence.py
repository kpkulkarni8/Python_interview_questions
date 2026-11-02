# Given a sentence, find the longest word without using built-in functions.

sentence = "Python programming is very interesting"

current_word = ""
longest_word = ""

for i in range(len(sentence)):

    if sentence[i] != " ":
        current_word = current_word + sentence[i]

    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word

        current_word = ""

# Check the final word because there is no space after it
if len(current_word) > len(longest_word):
    longest_word = current_word

print("Longest word:", longest_word)