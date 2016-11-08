from PIL import Image
img = Image.open('jenifer-gates.jpg').convert('L')
img.show()
img.save('jenifer-gates-bs.png')
