# -*- coding: utf-8 -*-
"""
@Copyright (C) 2021 mewhaku . All Rights Reserved 
@Time ： 2021/12/12 21:03
@Author ： mewhaku
@File ：read_and_load_picture.py
@IDE ：PyCharm
"""
import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt

#读取图像
img = cv.imread('D:\STUDY\graphy\img.jpg',0)
#利用opencv显示图像
cv.imshow('image',img)
#在matplotlib中显示图像
#plt.show()
k = cv.waitkey(10)
#保存图像
cv.imwrite('imh.png',img)

