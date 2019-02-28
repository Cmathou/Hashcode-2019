from img_sort import CreaSlide
from sort_by_tag_number import sort_tag

filein = ["a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt", "d_pet_pictures.txt", "e_shiny_selfies.txt"]
fileout = ["a_example_out.txt", "b_lovely_landscapes_out.txt", "c_memorable_moments_out.txt", "d_pet_pictures_out.txt", "e_shiny_selfies_out.txt"]

tags = []
slides = []
f = open(filein[1], "r")
nbr = int(f.readline())

for i in range(nbr) :
    line = f.readline()
    tag = line.split(" ")
    tag[1] = int(tag[1])
    tag[-1] = tag[-1].strip('\n')
    tags.append([i] + tag)
f.close()

tags = sort_tag(tags)

CreaSlide(0, tags, slides)
print(slides)

f = open(fileout[1], "w")
f.write(str(len(slides)) + '\n')
for e in slides:
    f.write(str(e) + '\n')
f.close()