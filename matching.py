# matching.py
# http://cons-robotics.com/API/matching.py

import numpy as np
import cv2
import pyautogui as pg
import time

def Screenshot():
	time.sleep(2)
	im = np.array(pg.screenshot('screen.jpg'))
	#print(im)
	return im

def ClickBOT(temp='template.jpg'):

	time.sleep(2)
	img = Screenshot()

	img_temp = cv2.imread(temp)
	#read image
	template = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY) #convert to gray image

	screen = cv2.imread('screen.jpg',cv2.IMREAD_GRAYSCALE)

	result = cv2.matchTemplate(template,screen, cv2.TM_CCOEFF_NORMED)

	#print(result)

	#checking location that's matched
	loc = np.where(result >=0.9)

	#print(loc)

	position = []

	for pt in zip(*loc):
		#print(pt)
		pos = (pt[1]+10,pt[0]+10) # pos = (371,24)	# for Windows
		#pos = ((pt[1]/2) +10,(pt[0]/2)+10)			# for Mac
		position.append(pos)

	print(position)
	pg.click(position[0])

	#cv2.imshow('img',img_temp)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

ClickBOT('test.jpg')