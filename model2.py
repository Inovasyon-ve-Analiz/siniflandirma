import torch

import pydicom
import cv2
import numpy as np
import matplotlib.pyplot as plt

import os

t = 5
i = 4
k = 7
x = 0
y = 0
w = 500
h = 500

dirs = ["INMEYOK","ISKEMI","KANAMA"]
for j,s in enumerate(dirs):
    for i,filename in enumerate(os.listdir("dataset\\TRAINING\\"+s+"\\PNG")):
        
        img = cv2.imread("dataset\\TRAINING\\"+s+"\\PNG\\"+filename)
        cimg = img[y:y+h,x:x+w,:]
        rimg = cimg.copy()
        gimg = cv2.cvtColor(cimg.copy(),cv2.COLOR_BGR2GRAY)
        _, th1 = cv2.threshold(gimg.copy(), t,255,cv2.THRESH_BINARY)
        dilation = cv2.erode(th1.copy(),np.ones((k,k),np.uint8),iterations=i)
        contours, _ = cv2.findContours(dilation.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        l = 0

        for c in contours:
            if len(c)>l:
                l=len(c)

                maxY = max(c.T[1][0])
                minY = min(c.T[1][0])
                maxX = max(c.T[0][0])
                minX = min(c.T[0][0])
        
        d = pydicom.read_file("dataset\\TRAINING\\"+s+"\\DICOM\\"+filename[:-4]+".dcm")
        print(type(d.pixel_array))
        break