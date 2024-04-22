import random

from cv2 import cv2
img=cv2.imread("2.PNG",1)

print(img)
print(type(img))
print(img.shape)

"""for i in range(100):
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]"""
vungchon=img[0:100,200:500]
img[300:400,500:800]=vungchon

cv2.imshow("anh",img)
cv2.waitKey()