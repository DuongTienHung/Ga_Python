import math
r= float(input("moi nhap vao ban kinh cua duong tron: "))
chuvi=2*r*math.pi
dientich= math.pi*(r**2)

print("chu vi hinh tron la: ",chuvi)
#2 cach 2 in thong bao ra man hinh
print(f"chu vi hinh tron la {chuvi}")

#3 cach 3
print("cach 3: chu vi la {}, dien tich la {}" .format(chuvi,dientich))
