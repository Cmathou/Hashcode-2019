import select
import calcul_score
from sort_by_tag_number import sort_tag

global tags
tags = []
f = open("a_example.txt", "r")
nbr = int(f.readline())

for i in range(nbr) :
    line = f.readline()
    tag = line.split(" ")
    tag[1] = int(tag[1])
    tag[-1] = tag[-1].strip('\n')
    tags.append([i] + tag)

tags = sort_tag(tags)