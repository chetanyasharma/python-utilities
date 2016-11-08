from PIL import Image
from pathlib import Path
t = raw_input("enter your path ") #this will take your image path from terminl
my_file = Path(t)
if my_file.is_file():
    img = Image.open(t)
    img.show()
    x = int(raw_input("enter first value"))
    y = int(raw_input("enter second value"))
    new_img = img.resize((x,y)) #this will resize your image
    new_img.save('jenifer-gates-x*y.jpg') #this will save your image
else:
    print "can't find image on this path. please enter a valid path "
