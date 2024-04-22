a=int(input("Nhap vao so a: "))
n=int(input("nhap vao n"))
if a%2 ==0:
    for i in range(1,n+1,1): #1,2,3,4,5
        print(i)
        a=a+i
    print("Tong a la : ", a)
else:
    print("tôi o tính tổng số lẻ, bye bye")