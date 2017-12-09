import cv2
import numpy as np
import os

def grab_number():
    # Needs to be a positive integer. I wanted to build a text parser.
    possible = '1234567890'
    num = ''
    while True:
        scrub = input('please input a positive integer: ')
        for i in scrub:
            if(i in possible):
                num += i
            elif(i == '.'):
                break
        try:
            int(num)
        except:
            pass
        else:
            break
    print(num , 'it is.')
    num = int(num)
    return num

def bify(num, img_name):
    img = cv2.imread(img_name)
    # Loop through and add
    res = img
    for i in range(num):
        res = cv2.add(res, img)
    cv2.imwrite("image1.png", res)
    return "image1.png"

def jpegify(num, img_name):
    # Begin jpegification
    img = cv2.imread(img_name)
    for i in range(num):
        name = img_name[:img_name.index('.')] + str(i) + '.jpeg'
        last_name = ''
        if(i == 0):
            last_name = img_name
        else:
            last_name = img_name[:img_name.index('.')] + str(i-1) + '.jpeg'
        img = cv2.imread(last_name)
        cv2.imwrite(name, img)
    # Delete all the images I made.
    for j in range(num-1):
        os.remove(img_name[:img_name.index('.')] + str(j) + '.jpeg')
    return img

def display(img):
    # Load image
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)

    # Clear on escape key
    k = cv2.waitKey(0)

    if(k == 27):
        cv2.destroyAllWindows()

def baf(before, after):
    # Load image
    cv2.namedWindow('before', cv2.WINDOW_NORMAL)
    cv2.namedWindow('after', cv2.WINDOW_NORMAL)

    cv2.imshow('before', before)
    cv2.imshow('after', after)

    # Clear on escape key
    k = cv2.waitKey(0)

    if(k == 27):
        cv2.destroyAllWindows()
