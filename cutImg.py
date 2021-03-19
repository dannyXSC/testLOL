from PIL import Image

path = "D:\\MyProject\\python\\testLOL\\picture"
img = Image.open(path + "\\mainTest.png")
print(img.size)
startX = 15
startY = img.size[1] * 0.75
width = img.size[0] * 0.1
height = img.size[1] * 0.15
cropped = img.crop((startX, startY, startX + width, startY + height))
cropped.save(path + "\\cut.png")
