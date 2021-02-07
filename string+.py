words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []

for word in words:
    if word[-1] == 'e':
        word = word + 'd'
    else:
        word = word + 'ed'
    past_tense.append(word)

print(words)
print(past_tense)    # NOTE:
        # past_tense.append(a)
    # elif a[-1] == 'e':
        # a.append('d')
        # past_tense.append(a)
    # else:
    #     pass

# print(past_tense)
