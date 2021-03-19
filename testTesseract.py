import pytesseract
import cv2
from PIL import Image
im = Image.open("D:/MyProject/python/testLOL/picture/afterProcess.png")
widthAll = im.size[0]
heightAll = im.size[1]
im.crop()

print(pytesseract.image_to_string(im, lang='eng'))