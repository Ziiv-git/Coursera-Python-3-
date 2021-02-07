#Write a function, sublist, that takes in a list of numbers as the parameter.
#In the function, use a while loop to return a sublist of the input list.
#The sublist should contain the same values of the original list up until it reaches
#the number 5 (it should not contain the number 5).
# NOTE:

def sublist(l):
    new_list = []
    id = 0
    while id <= (len(l)-1):
        if l[id] ==5:
            break
        else:
            new_list.append(l[id])
        id = id + 1
    return new_list

print(sublist([1,2,3,4,5,6,7,8,9,0]))
