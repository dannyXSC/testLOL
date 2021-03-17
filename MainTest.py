import pyautogui as pag
import time
import asyncio

screenWidth,screenHeight=pag.size()
startX=screenWidth/9*3
startY=screenHeight/5*4
chessWidth=screenWidth/9

async def async_LoLclick(num):
    distance=200
    while distance>0:
        pag.drag()

async def click(num):
    print(f"go to {num}...")
    await async_LoLclick(num)
    print(f"...successfully go to {num}")

async def main():
    await asyncio.gather(click(1),click(2),click(3),click(4),click(5))

asyncio.run(main())

# for i in range(2, 11):
#     #用0.5 秒的时间把光标移动到(400, 175 + i * 20) 位置
#     pyautogui.moveTo(0,1800,duration = 0.5)
#     # pyautogui.click(clicks = 2, button ='left', interval = 0.05)# 点击进入单据
#     # time.sleep(3)
#     # pyautogui.click(100, 140)# 点击修改
#     # time.sleep(3)
#     # pyautogui.click(350, 190, button ='left')# 左击发货日
#     # pyautogui.click(350, 190, button ='right')# 右击发货日
#     # time.sleep(1.5)
#     # pyautogui.click(595, 397)# 选择日期5
#     # time.sleep(1.5)
#     # pyautogui.click(815, 472)# 完成
#     # time.sleep(1.5)
#     # pyautogui.click(565, 425)# 发出日大于接收日， 是
#     # time.sleep(1.5)
#     # pyautogui.click(155, 140)# 点击保存
#     # time.sleep(2)
#     # pyautogui.click(432, 140)# 点击查询
#     # time.sleep(5)