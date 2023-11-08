#!/usr/bin/python3
def search_replace(my_list, search, replace):
    L = my_list.copy()
    x = 0
    for i in L:
        if(i==search):
            L[x] = replace
        x+=1
    return L
