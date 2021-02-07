stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
s = 'The water earth and air are vital'
new_sentence = s.split()
acro_list = []

for acronym in new_sentence:
    if acronym in stopwords:
        pass
    else:
        acro_list.append(acronym[0:2].upper())

s = '. '
acro = s.join(acro_list)
print(acro)
