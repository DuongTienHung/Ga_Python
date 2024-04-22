from cv2 import cv2
# doc anh
img=cv2.imread("2.PNG",1)

#resize image
#img=cv2.resize(img,(100,200)) # rog,dai
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)

#xoay anh
img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
# xuat anh
cv2.imshow("cua so hien thi",img)
k=cv2.waitKey()
print(k)
if k==ord("s"):
    cv2.imwrite("anhmoi.jpg",img)
