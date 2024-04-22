from math import sqrt
print("Day la chuong trinh giai phuong trinh bac 2 ")
a =float(input("nhap vao gia tri cua a trong bieu thuc ax^2 + bx + c =0: "))
b =float(input("nhap vao gia tri cua b trong bieu thuc ax^2 + bx + c =0: "))
c =float(input("nhap vao gia tri cua c trong bieu thuc ax^2 + bx + c =0: "))

#voi a#0
delta =(b**2)-(4*a*c)
if delta <0:
    print("phuong trinh vo nghiem")
elif delta ==0:
    print("phuong trinh co nghiem kep x1=x2= ", -b/(2*a))
else:
    print("phuong trinh co 2 nghiem phan biet")
    x1= (-b+sqrt(delta))/(2*a)
    x2= (-b-sqrt(delta))/(2*a)
    print("x1 =", x1)
    print("x2 =", x2)


