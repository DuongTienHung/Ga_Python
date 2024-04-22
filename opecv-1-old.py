from cv2 import cv2
img=cv2.imread("2.PNG",1) # doc anh
#img=cv2.resize(img,(400,200))  # dua kich thuoc anh
img=cv2.resize(img,(0,0), fx=0.25,fy=0.25)  #(fx rộng, fy dài )
img=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("hien thi anh",img)
k=cv2.waitKey()
print(k)
print(ord("s"))
if k == ord("s"):
    cv2.imwrite("anhmoi.jpg", img)


