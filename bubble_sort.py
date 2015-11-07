unsorted_list = [9, 2, 4, 8, 5, 2, 8, 1, 2, 6, 3]


def bubble_sorter(_list):
    not_sorted = []
    while True:
        if len(not_sorted) + 1 == len(_list):
            break
        not_sorted = []
        for index, i in enumerate(_list[:-1]):
            if _list[index] > _list[index + 1]:
                move_forward = _list[index + 1]
                del _list[index + 1]
                _list.insert(move_forward, index)
            else:
                not_sorted.append(True)
    return _list

sorted_list = bubble_sorter(unsorted_list)

print(sorted_list)
