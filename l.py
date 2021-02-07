def beginning(a):
    new_list = []
    id = 0

    while id <= (len(a)-1):
        if a[id] == 'bye':
            break
        elif id >= 10:
            break
        else:
            new_list.append(a[id])
        id = id + 1
    return new_list

print(beginning(['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']))
