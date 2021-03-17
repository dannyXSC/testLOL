from PyQt5.QtWidgets import QApplication
import PyQt5.QtGui as QtGui
import win32gui
import sys
import numpy as np


def qimage2numpy(qimage, dtype='array'):
    """Convert QImage to numpy.ndarray.  The dtype defaults to uint8
    for QImage.Format_Indexed8 or `bgra_dtype` (i.e. a record array)
    for 32bit color images.  You can pass a different dtype to use, or
    'array' to get a 3D uint8 array for color images."""
    result_shape = (qimage.height(), qimage.width())
    temp_shape = (qimage.height(), qimage.bytesPerLine() * 8 / qimage.depth())
    if qimage.format() in (QtGui.QImage.Format_ARGB32_Premultiplied,
                           QtGui.QImage.Format_ARGB32,
                           QtGui.QImage.Format_RGB32):
        if dtype == 'rec':
            dtype = QtGui.bgra_dtype
        elif dtype == 'array':
            dtype = np.uint8
            result_shape += (4, )
            temp_shape += (4, )
    elif qimage.format() == QtGui.QImage.Format_Indexed8:
        dtype = np.uint8
    else:
        raise ValueError("qimage2numpy only supports 32bit and 8bit images")
        # FIXME: raise error if alignment does not match
    buf = qimage.bits().asstring(qimage.numBytes())
    result = np.frombuffer(buf, dtype).reshape(temp_shape)
    if result_shape != temp_shape:
        result = result[:, :result_shape[1]]
    if qimage.format() == QtGui.QImage.Format_RGB32 and dtype == np.uint8:
        result = result[..., :3]
    result = result[:, :, ::-1]
    return result


hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd, 0, 0, 100, 100).toImage()
print(qimage2numpy(img))