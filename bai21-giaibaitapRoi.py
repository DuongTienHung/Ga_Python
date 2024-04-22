def roi(dt,cp):
    return (dt-cp)/cp
def QuyetDinhDauTu(roi):
    if roi>=0.75:
        return "Nen dau tu"
    else:
        return "Khong nen dau tu"

print("chuong trinh tinh roi")
cp=float(input("nhap vao chi phi: "))
dt=float(input("nhap vao doanh thu: "))
b=roi(dt,cp)
a=QuyetDinhDauTu(b)
print(a)
print(f"Ty le roi la {b}")