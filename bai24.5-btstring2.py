n=input("Mời thím nhập mật khẩu: ")
x=bool
y=bool
#print(x,y)

for i in n:
    if i.isdigit():
        x=True
        break
    else:
        x=False
for i in n:
    if i.isalpha():
        y=True
        break
    else:
        y=False
while len(n)<6 or x==False or y==False :
    n=input("Nhập lại MK, ít nhất 6 ký tự, ít nhất 1 chữ cái và 1 số")
else:
    print("Mật khẩu hợp lệ")