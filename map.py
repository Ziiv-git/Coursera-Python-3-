def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)

# NOTE: see the difference between first and second program in this page
# NOTE: basically map is a for which it does in the background

def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)


things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))


lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def doubled(s):
    return s*2
greeting_doubled = map(doubled,lst)
print(greeting_doubled)

g_d = map(lambda a:a*2, lst)
print(g_d)


abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = map(lambda u:u.upper(), abbrevs)
print(abbrevs_upper)

abbrevs_up2 = map(lambda u:u[1].upper(), abbrevs)
print(abbrevs_up2)
