from Frame import Framework
from ChessInformation import chessInformation

picutre_path = "D:/MyProject/python/testLOL/picture/"

frame = Framework()
imgHandle = chessInformation()
# for i in range(5):
#     img = imgHandle.getChessImg(i, frame)
#     img.save(picutre_path + "/mainTest" + str(i) + ".png", "png")
print(frame.dButton_X, frame.dButton_Y, frame.dButton_width,
      frame.dButton_height)
img = imgHandle.getImg(int(frame.dButton_X), int(frame.dButton_Y),
                       int(frame.dButton_width), int(frame.dButton_height))
img.save(picutre_path + "/dButton.png", "png")
