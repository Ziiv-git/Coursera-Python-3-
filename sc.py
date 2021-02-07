
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

for word in positive_words:
    word.lower()

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

for word in negative_words:
    word.lower()

def strip_punctuation(text):
    no_punctuation = ""
    for char in text:
         if char not in punctuation_chars:
            no_punctuation = no_punctuation + char
    return no_punctuation

def get_pos(s):
    a = strip_punctuation(s)
    b = a.lower().split()
    pos_words = 0
    for word in b:
        if word in positive_words:
            pos_words = pos_words + 1
        else:
            pass
    return pos_words

def get_neg(s):
    a = strip_punctuation(s)
    b = a.lower().split()
    neg_words = 0
    for word in b:
        if word in negative_words:
            neg_words = neg_words + 1
        else:
            pass
    return neg_words

with open('project_twitter_data.csv','r') as twitter:
    data = twitter.readlines()

outfile=open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")
for i in data[1:]:
    res_row=""
    splt=i.strip().split(",")           #Leading and trailing whitespaces are removed with strip
    res_row=("{},{},{},{},{}".format(splt[1], splt[2], get_pos(splt[0]), get_neg(splt[0]), (get_pos(splt[0])-get_neg(splt[0]))))
    outfile.write(res_row)
    outfile.write("\n")
outfile.close()
