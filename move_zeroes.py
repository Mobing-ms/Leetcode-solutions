lists = [0,1,0,3,12]

def move_to_end(lists):
    for i in lists:
        if i == 0:
            lists.remove(i)
            lists.append(0)

    return lists

new_list = move_to_end(lists)
print(new_list)
