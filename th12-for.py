# TH12 tính tổng s= 1!+2!+3!+....+10!
m=1
tong=0
for i in range(1,11,1):
    m=i*m
    tong=tong+m
print("tong cac so tui 1 den 10 giai thua la: ",tong)