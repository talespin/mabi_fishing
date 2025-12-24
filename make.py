import cv2
import pyautogui as auto
from time import sleep
from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops


box_area = (790, 960, 830, 1000)
for i in range(300):
    img_arrow = ImageGrab.grab(box_area)
    img_arrow.save(f'image/arrow{i}.png')
    sleep(0.02)


def main():
    auto.mouseInfo()
    box_area = (790, 960, 830, 1000)
    input('arrow image')
    img_arrow = ImageGrab.grab(box_area)
    img_arrow.save('image/arrow.png')
    input('fishing image')
    img_fishing = ImageGrab.grab(box_area)
    img_fishing.save('image/fishing.png')
    input('ready image')
    img_ready = ImageGrab.grab(box_area)
    img_ready.save('image/ready.png')
    input('space image')
    img_space = ImageGrab.grab(box_area)
    img_space.save('image/space.png')



#if __name__=='__main__':
#    main()


"""
아래 이미지 4개를 떠놔야함
arrow.png
fishing.png
ready.png
space.png
"""
