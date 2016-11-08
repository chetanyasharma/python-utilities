from PIL import Image
from pathlib import Path
t = raw_input("enter your path ")
my_file = Path(t)
if my_file.is_file():
    img = Image.open(t)
    img.show()
    x = int(raw_input("enter first value"))
    y = int(raw_input("enter second value"))
    new_img = img.resize((x,y))
    new_img.save('jenifer-gates-x*y.jpg')
else:
    print "can't find image on this path. please enter a valid path "
