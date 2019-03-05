# -*- coding: utf-8 -*-
def sort_tag_lent(list_tot):
    list_nb_tags = []
    sorted_list_tot = []
    for elem in list_tot:
        list_nb_tags += [elem[2]]

    sorted_list_nb_tags = sorted(list_nb_tags)
    sorted_list_nb_tags = sorted_list_nb_tags[::-1]
    
    
    for qte in sorted_list_nb_tags:
        for elem in list_tot:
            if elem[2] == qte:
                new_elem = list_tot.pop(list_tot.index(elem))
                sorted_list_tot += [new_elem]

    return sorted_list_tot

def sort_tag(tag_list):
    sorted_list = []
    tag_len = len(tag_list)
    a_size = tag_len//2
    if tag_len < 2:
        return tag_list
    a = sort_tag(tag_list[:a_size])
    b = sort_tag(tag_list[a_size:])
    while len(a)>0 and len(b)>0:
        if a[0][2] < b[0][2]:
            sorted_list.append(a[0])
            del a[0]
        else:
            sorted_list.append(b[0])
            del b[0]
    if len(a)>0:
        sorted_list += a
    else:
        sorted_list += b
    return sorted_list