def rotate_left_list(my_list=[], number_rotation=0):
    new_list = my_list.copy()
    num = 0
    for i in range(number_rotation):
        num = new_list[0]
        new_list.reverse()
        new_list.pop()
        new_list.reverse()
        new_list.append(num)
    return new_list
