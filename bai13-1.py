while True:
    hten=input("nhap ten: ")
    mhoc=input("nhap mon hoc: ")
    diem=float(input("nhap diem: "))
    print(f"hoc sinh {hten}, du thi mon {mhoc}, co so diem {diem}")
    if diem>=7:
        print("Xep loai diem : Dat")
    else:
        print("xep loai diem: KHONG DAT")
    hoi=input("nhap n de thoat, hoac bam phim bat ky de tiep tuc: ")
    if hoi=="n" or hoi=="N":
        break
