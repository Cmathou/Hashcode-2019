# -*- coding: utf-8 -*-
def sort_tag(list_tot):
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