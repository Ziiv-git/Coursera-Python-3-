data = ['Writing', 'essays', 'for', 'school', 'can', 'be', 'difficult', 'but', 'many', 'students', 'find', 'that', 'by', 'researching', 'their', 'topic', 'that', 'they', 'have', 'more', 'to', 'say', 'and', 'are', 'better', 'informed.', 'Here', 'are', 'the', 'university', 'we', 'require', 'many', 'undergraduate', 'students', 'to', 'take', 'a', 'first', 'year', 'writing', 'requirement', 'so', 'that', 'they', 'can', 'have', 'a', 'solid', 'foundation', 'for', 'their', 'writing', 'skills.', 'This', 'comes', 'in', 'handy', 'for', 'many', 'students.', 'Different', 'schools', 'have', 'different', 'requirements,', 'but', 'everyone', 'uses', 'writing', 'at', 'some', 'point', 'in', 'their', 'academic', 'career,', 'be', 'it', 'essays,', 'research', 'papers,', 'technical', 'write', 'ups,', 'or', 'scripts.']

p_words = []
for word in data:
    if 'p' in word:
        p_words.append(word)
    else:
        pass
print(p_words)



sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
new_sentence = sentence.split(' ')
print(new_sentence)

repeat = {}

for word in new_sentence:
    if word not in repeat:
        repeat[word] = 0
    repeat[word] = repeat[word] + 1

for word in repeat.keys():
    print(word + ':' + str(repeat[word]) + " occurence")
