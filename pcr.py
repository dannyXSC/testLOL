import threading
import time
import inspect
import ctypes
import pyautogui
import keyboard


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,
                                                     ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def press():
    time.sleep(2)
    for j in range(1, 3):
        pyautogui.click(1109, 568, 1)
        time.sleep(2)
        pyautogui.click(1600, 870, 1)
        time.sleep(2)
        pyautogui.click(1600, 870, 1)
        time.sleep(2)
        sleepTime = 0.5
        for i in range(1, 1200):  #1500
            time.sleep(sleepTime)
            pyautogui.click(535, 855, 1)
            time.sleep(sleepTime)
            pyautogui.click(750, 855, 1)
            time.sleep(sleepTime)
            pyautogui.click(965, 855, 1)
            time.sleep(sleepTime)
            pyautogui.click(1180, 855, 1)
            time.sleep(sleepTime)
            pyautogui.click(1395, 855, 1)
        pyautogui.click(1572, 943, 1)
        time.sleep(3)


if __name__ == "__main__":
    t = threading.Thread(target=press, args=[])
    t.start()
    time.sleep(0.001)
    print("hello")
    keyboard.wait('f1')
    stop_thread(t)
    print("stoped")