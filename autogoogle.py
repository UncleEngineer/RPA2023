import webbrowser
import time
import pyautogui as pg

webbrowser.open('https://www.google.com')
time.sleep(2)

pg.write('jpy to thb')
time.sleep(2)
pg.press('enter')
time.sleep(2)
pg.screenshot('jpy to thb.png')
