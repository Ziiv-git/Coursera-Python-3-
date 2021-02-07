original_str = "The quick brown rhino jumped over the extremely lazy fox"
new_str = original_str.split(' ')
print(new_str)
a = None
num_word_list = []
for word in new_str:
    if a is None:
        a = word
    num_word_list.append(len(word))
    a = word
print(num_word_list)
