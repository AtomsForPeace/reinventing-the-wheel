sorted_list = []
unsorted_list = [9, 2, 4, 8, 5, 2, 8, 1, 2, 6, 3]


def insertion_sorter():
    sorted_list.append(unsorted_list[0])
    for to_insert in unsorted_list[1:]:
        check_point = -1
        while True:
            if len(sorted_list) < abs(check_point):
                sorted_list.insert(0, to_insert)
            elif sorted_list[check_point] > to_insert:
                check_point -= 1
            else:
                sorted_list.insert(check_point + 1, to_insert)
                break

insertion_sorter()

print(sorted_list)
