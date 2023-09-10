#!/usr/bin/pyrhon3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
        else:
            return my_list.insert(idx, element)
