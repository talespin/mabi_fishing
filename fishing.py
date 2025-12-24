import cv2
import pyautogui as auto
from time import sleep
from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops


def hist_score(image1,image2):
    ## 히스토그램 유사도
    hsv1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
    # 히스토그램 계산
    hist1 = cv2.calcHist([hsv1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([hsv2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist_similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return hist_similarity


def main():
    box_area = (790, 960, 830, 1000)
    img_arrow = [cv2.imread(f'image/arrow{x}.png') for x in range(300)]
    img_fishing = cv2.imread('image/fishing.png')
    img_ready = cv2.imread('image/ready.png')
    img_space = cv2.imread('image/space.png')
    while True:
        try:
            sleep(0.05)
            img = ImageGrab.grab(box_area)
            img.save('image/test.png')
            img_test = cv2.imread('image/test.png')
            if max([hist_score(img_test, x) for x in img_arrow]) > 0.9:
                print('arrow state')
                auto.moveTo(400, 980)
                auto.click()
                auto.dragTo(20, 0, duration=0.3, button='left')
                sleep(0.2)
            elif hist_score(img_test, img_fishing) > 0.8:
                print('fishing state')
                auto.moveTo(810, 980)
                auto.click()
                auto.moveTo(114, 280)
                auto.click()
                sleep(0.7)
            elif hist_score(img_test, img_ready) > 0.8:
                print('ready state')
            elif hist_score(img_test, img_space) > 0.8:
                print('space state')
            else:
                print('unknown')
            sleep(0.02)
        except KeyboardInterrupt:
            return        
        except:
            pass


if __name__=='__main__':
    sleep(3)
    main()


"""
아래 이미지 4개를 떠놔야함
arrow.png
fishing.png
ready.png
space.png
"""
