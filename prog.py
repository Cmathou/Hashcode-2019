from img_sort import CreaSlide
from sort_by_tag_number import sort_tag

tags = []
slides = []
f = open("a_example.txt", "r")
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

f = open("a_example_out.txt", "w")
f.write(str(len(slides)) + '\n')
for e in slides:
    f.write(str(e) + '\n')
f.close()