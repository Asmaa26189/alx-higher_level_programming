#!/usr/bin/env python3
def no_c(my_string):
    # new_string = ""
    # for x in my_string:
    #     if x !='c' and x != 'C':
    #         new_string += x
    new_string = [x for x in my_string if x !='c' and x != 'C']
    return ("".join(new_string))
