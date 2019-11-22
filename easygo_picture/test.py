# -*- coding: utf-8 -*-
''''
import os 
import shutil
main_path = r'D:/3'
for i in os.listdir(main_path):
    if os.path.isdir(os.path.join(main_path,i)):
        j = os.listdir(os.path.join(main_path,i,'jpg'))
        shutil.copy(os.path.join(main_path,i,'jpg',j[0]), main_path)
        os.rename(os.path.join(main_path,j[0]), os.path.join(main_path,i+'.jpg'))
        '''
import cv2
image = cv2.imread('D:/input/3/16_1559825195_09_50/jpg/201906061951280000.jpg')
print(image.shape)