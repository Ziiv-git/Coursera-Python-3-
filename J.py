def stop_at_four(l):
    new_list = []
    id = 0
    while id <= (len(l)):
        if l[id] == 4:
            break
        else:
            new_list.append(l[id])
        id = id + 1
    return new_list

print(stop_at_four([0, 9, 4.5, 1, 7]))
