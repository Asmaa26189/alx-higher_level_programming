#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = []
    if(idx < 0 or idx >=  len(my_list)):
        return my_list
    else:
        # for x in my_list:
        #     newList.append(x)
        newList = [x for x in my_list]
        newList[idx] = element
        return newList
