import pyautogui
import os
import asyncio
import time

screenWidth,screenHeight=pyautogui.size()
dis = int(screenWidth/4)
dea = int(dis/20)

async def async_drawMatrix(startX,startY,distance,decrease):
    dur=0.01
    pyautogui.moveTo(startX,startY,duration=dur)

    while distance > 0:
        pyautogui.drag(distance, 0, duration=dur)   # move right
        distance -= decrease
        await asyncio.sleep(0.5)

        pyautogui.drag(0, distance, duration=dur)   # move down
        await asyncio.sleep(0.5)

        pyautogui.drag(-distance, 0, duration=dur)  # move left
        distance -= decrease
        await asyncio.sleep(0.5)

        pyautogui.drag(0, -distance, duration=dur)  # move up
        await asyncio.sleep(0.5)

async def fun():
    print("hello")
    await asyncio.sleep(1)

async def async_main():
    await asyncio.gather( *(async_drawMatrix(screenWidth/8,screenHeight/8,dis,dea),fun()))

asyncio.run(async_main())
