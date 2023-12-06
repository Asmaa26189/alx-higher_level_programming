#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = ''
    big = 0
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret = k
    return (ret)
