a="English =78 Science = 83 Math = 68 History = 65"
tach=a.split()
s=0
dem=0
for i in tach:
    if i.isdigit():
        s=s+int(i)
        dem=dem+1 #dem+=1

print(f"Tong cac chu so trong chuoi tren la: {s}" )
print(f"trung binh cong cua cac so trong chuoi tren la: {s/dem}" )

