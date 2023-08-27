import pyautogui as pg
import os
import subprocess
import time

#subprocess.Popen('mspaint.exe')

time.sleep(1)

location = pg.locateOnScreen('brush_on.png')
# print(location)

# if location != None:
#     pg.moveTo(200,200)
#     pg.dragTo(500,500,button='left')

location = pg.locateOnScreen('bubble.png')
print('Bubble:',location)

print(location.left,location.top)

if location.left <= 600 and location.top <=600:
    pg.click('bubble.png',clicks=3)
    time.sleep(0.5)
    pg.moveTo(200,200)
    pg.dragTo(500,500,button='left')

























# path = os.getcwd() # current working directory
# print(path)
# image = 'brush.png'
# fullpath = os.path.join(path,image)
# print(fullpath)
# folder = 'img'
# fullpath_folder = os.path.join(path,folder)
# fullpath_image_folder = os.path.join(fullpath_folder,image)
# print(fullpath_image_folder)