import pyautogui as py,time
from PIL import ImageGrab,ImageOps,Image
from numpy import *
import numpy

#6791
def obstacleDetector():
    area = (166, 417, 342 , 480)
    avoid = ImageGrab.grab(area)
    grayAvoid = ImageOps.grayscale(avoid)
    areay = array(grayAvoid.getcolors())
    return areay.sum()

def obstacleEnder():
    sth = True
    area = (170, 417, 346, 480)
    area2 = (170, 616, 346, 679)
    avoid = ImageGrab.grab(area)
    avoid2 = ImageGrab.grab(area2)
    px = avoid.load()
    py = avoid2.load()
    for x in range(176):
        for y in range(63):
            if px[x, y] != py[x, y]:
                sth = False
                break
    return sth
def obstacleDestroyeruwu():
    indx = 0
    area = (160, 400, 354, 480)
    area2 = (160, 616, 354, 679)
    avoid = ImageGrab.grab(area)
    avoid2 = ImageGrab.grab(area2)
    px = avoid.load()
    py = avoid2.load()
    if px[120, 72] != py[1, 1]:
        indx = 1

    if px[101, 72] != py[1, 1]:
        indx = 1


    return indx


def click():
    py.keyDown("space")
    time.sleep(0.1)
    py.keyUp("space")

def duck():
    py.keyDown("down")
    time.sleep(0.1)
    py.keyUp("down")

def run():
    py.click(320, 20)
    py.click(715, 413)

def main():
    run()
    #while True:
        #area = (166, 417, 342 , 480)
        #avoid = ImageGrab.grab(area)
        #grayAvoid = ImageOps.grayscale(avoid)
        #areay = array(grayAvoid.getcolors())
        #print(areay.sum())

    while True:
        ob = obstacleEnder()
        if ob == False :
            click()


if __name__ == '__main__':
    main()

