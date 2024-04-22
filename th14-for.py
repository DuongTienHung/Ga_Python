# TH15: tính tổng s(x,n) = x + (X^2 /2!) +...+ (X^n /n!)
x=int(input("nhap vao x: "))
n=int(input("nhap vao n: "))
for a in range(1,n+1,1):
    tu=(x**a)
    mau=1
    for