t =int(input("moi thi chu nhap vao so thang: "))
if t in (1,3,5,7,8,12):
    print(f"Bam cu thang {t} co 31 ngay ")
elif t in (4,6,9,11):
    print(f"Bam cu thang {t} co 30 ngay")
elif t==2:
    n=int(input("vui long nhap them nam: "))
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print(f"thang {t} nam {n} co 29 ngay ")
    else:
        print(f"thang {t} nam {n} co 28 ngay ")
else:
    print("ban nhap sai du lieu thang")


