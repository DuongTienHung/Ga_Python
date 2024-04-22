dtb=float(input("moi nhap vao diem trung binh: "))
if dtb>=9.0:
    print("Ban dat loai gioi, diem trung binh cua ban la" , dtb)
elif dtb>=7.0 and dtb<9.0:
    print(f"ban dat loai kha, diem trung binh cua ban la {dtb}")
elif 5.0<=dtb<7.0:
    print("ban dat loai Trung binh, diem trung binh cua ban la {}" .format(dtb))
else:
    print("ban dat loai yeu, diem trung binh cua ban la ", dtb)