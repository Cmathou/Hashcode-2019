from img_sort import CreaSlide
from sort_by_tag_number import sort_tag
from math import ceil

filein = ["a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt", "d_pet_pictures.txt", "e_shiny_selfies.txt"]
fileout = ["a_example_out.txt", "b_lovely_landscapes_out.txt", "c_memorable_moments_out.txt", "d_pet_pictures_out.txt", "e_shiny_selfies_out.txt"]

part = 1000
file_nbr = 0
tags = []
tagsV = []
slides = []
f = open(filein[file_nbr], "r")
nbr = int(f.readline())

for i in range(nbr) :
    line = f.readline()
    tag = line.split(" ")
    tag[1] = int(tag[1])
    tag[-1] = tag[-1].strip('\n')
    if tag[0] == 'H':
        tags.append([i] + tag)
    else:
        tagsV.append([i] + tag)
f.close()

f = open(fileout[file_nbr], "w")
f.write(str(int(len(tags)+len(tagsV)/2)) + '\n')

tags = sort_tag(tags)
tagsV = sort_tag(tagsV)
tagsize = len(tags)
tagvsize = len(tagsV)

# sort H img
for  i in range(int(ceil(1.0*tagsize/part))):
    print("i = "+str(i))
    slides = []
    if part*(i+1) < tagsize:
        CreaSlide(0, tags[part*i:part*(i+1)], slides)
        for e in slides:
            f.write(str(e) + '\n')
    else:
        CreaSlide(0, tags[part*i:], slides)
        for e in slides:
            f.write(str(e) + '\n')

#sort V img
for  i in range(int(ceil(1.0*tagvsize/part))):
    print("i = "+str(i))
    slides = []
    if part*(i+1) < tagvsize:
        CreaSlide(0, tagsV[part*i:part*(i+1)], slides)
        for i in range(len(tagsV)//2):
            f.write(str(tagsV[2*i][0]) + " " + str(tagsV[2*i+1][0]) + '\n')
    else:
        CreaSlide(0, tagsV[part*i:], slides)
        for i in range(len(tagsV)//2):
            f.write(str(tagsV[2*i][0]) + " " + str(tagsV[2*i+1][0]) + '\n')

f.close()