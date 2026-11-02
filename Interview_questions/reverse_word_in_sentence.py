# Given a sentence, reverse the order of the words without reversing the individual words.

sentence = "Python is very interesting"

reversed_sentence = ""
current_word = ""

for i in range(len(sentence)):

    if sentence[i] != " ":
        current_word = current_word + sentence[i]

    else:
        reversed_sentence = current_word + " " + reversed_sentence
        current_word = ""

# Add the last word
reversed_sentence = current_word + " " + reversed_sentence

# Remove the final extra space manually
if len(reversed_sentence) > 0:
    reversed_sentence = reversed_sentence[:len(reversed_sentence)-1]

print(reversed_sentence)

