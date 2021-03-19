from PyQt5.QtWidgets import QApplication
import PyQt5.QtGui as QtGui
from PyQt5.QtCore import QBuffer
import win32gui
import sys
import numpy as np
from PIL import Image
import io

picutre_path = "D:/MyProject/python/testLOL/picture/"


def convertQImageToMat(incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''

    incomingImage = incomingImage.convertToFormat(4)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  #  Copies the data
    return arr


import io
from PIL import Image
from PyQt5.QtGui import QImage
import numpy as np
from PyQt5.QtCore import QBuffer


def QImage2PILImage(img):
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    img.save(buffer, "PNG")
    pil_im = Image.open(io.BytesIO(buffer.data()))
    return pil_im


hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd, 0, 0, 100, 100).toImage()
img.save(picutre_path + "/1.png", "PNG")
img_pil = QImage2PILImage(img)
img_pil_arr = np.array(img_pil)
img_open = Image.open(picutre_path + "1.png")
img_open_arr = np.array(img_open)
img_convert = convertQImageToMat(img)

# print(type(img_pil))
# print(type(img))
# print(type(img_open))

#print(img_convert)
img_pil.save(picutre_path + "pil_1.png", "png")

#print(img_open_arr.shape, img_convert.shape)
# print(np.array_equal(img_open, convertQImageToMat(img)))
