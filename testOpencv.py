import cv2
import matplotlib.pyplot as plt
from PIL import Image

path = "D:/MyProject/python/testLOL/picture/"

img = cv2.imread(path + '/mainTest.png', 0)  #直接读为灰度图像
threshValue1 = 123
threshValue2 = 255
ret, thresh1 = cv2.threshold(img, threshValue1, threshValue2,
                             cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, threshValue1, threshValue2,
                             cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, threshValue1, threshValue2, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, threshValue1, threshValue2,
                             cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, threshValue1, threshValue2,
                             cv2.THRESH_TOZERO_INV)
img_out = Image.fromarray(thresh2)
img_out.save(path + "\\afterProcess.png", "png")
titles = ['img', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()