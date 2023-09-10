def element_at(my_list, idx):
    for e in range(len(my_list)):
        if idx < 0 or idx > range(len(my_list)):
            return None
        else:
            print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
