ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(str):
    return str[1]
 #returning the second letter on any string

sorted_by_second_let=sorted(ex_lst,key=second_let)
print (sorted_by_second_let)
