#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    b = len(my_list)
    if idx >= 0 and idx < b:
        del my_list[idx]
    return my_list
