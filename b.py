sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
new_sentence = sentence.split(' ')
words = 0
same_letter_count = []
print(new_sentence)

for word in new_sentence:
    if word[0] == 's':
        print(word)
        same_letter_count.append(word)
        words += 1
    else:
        pass

print(same_letter_count)
print(words)
