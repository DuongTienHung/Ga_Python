t=int(input("nhap vao 1 thang bat ky 1-12: "))
if t in (1,2,3):
    print(f"thang {t} thuoc quy 1")
elif t in (4,5,6):
    print(f"thang {t} thuoc quy 2")
elif t in (7,8,9):
    print(f"thang {t} thuoc quy 3")
elif t in (10,11,12):
    print(f"thang {t} thuoc quy 4")
else:
    print(f"ban nhap sai du lieu thang, khong co thang {t} tren lich")
