"""
1. viết chương trình kiểm tra tính hợp lệ của mật khẩu, mật khẩu hợp lệ khi có ít nhất 6 ký tự
chứa ít nhất 1 chữ cái ( chũ cái thường hoặc hoa đều được)
chứa ít nhất 1 chữ số

2. cho người dùng nhập vào mật khẩu để login /
so sánh, nếu đúng mở của, sai quá 5 lần khóa đăng nhập, thoát chương trình
"""
n=input("Mời thím nhập mật khẩu: ")
x=bool
y=bool



#print(x,y)
while True:
    for i in n:
        if i.isdigit():
            x = True
            break
        else:
            x = False
    for i in n:
        if i.isalpha():
            y = True
            break
        else:
            y = False
    if len(n)<6 or x==False or y==False:
        n=input("Nhập lại MK, ít nhất 6 ký tự, ít nhất 1 chữ cái và 1 số")
    else:
        print("Mật khẩu hợp lệ")
        break



#2: y so 2
s = input("Mời nhập mật khẩu đăng nhập hệ thống : ")
dem=0
while s!=n:
    dem=dem+1
    s = input(f"Nhập lại mật khẩu( bạn đã nhập sai {dem}/5 lần)  : ")
    if dem==4:
        print("Bạn nhập sai quá 5 lần, khóa đăng nhập")
        break
else:
    print("Đăng nhập hệ thống thành công")