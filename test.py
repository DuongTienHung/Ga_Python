lst=["6B 7C AB FE FF","7B 7C AB FE FF","8B 7C AB FE FF","9B 7C AB FE FF","5B 7C AB FE FF"]
mk="mo cua ra nhanh len"
s=input("Mời quét thẻ đăng nhập : ")
import time
d=""

while True:
    dem = 0
    while (s in lst) == False:
        dem = dem + 1
        s = input(f"quét lại thẻ, quét sai {dem}/5 lần")
        if dem == 4:
            print("Quét sai thẻ quá 5 lần, thoát hệ thống")
            break
    else:
        print("Đăng nhập thành công")
        log=True




    d = input("Mời nhập mật khẩu đăng nhập hệ thống : ")
    dem=0
    while d!=mk:
        dem=dem+1
        d = input(f"Nhập lại mật khẩu( bạn đã nhập sai {dem}/3 lần)  : ")
        if dem==2:
            print("Bạn nhập sai quá 3 lần, khóa đăng nhập")
            break
    else:
        print("Mở cửa thành công, cửa khóa sau 2s")
        time.sleep(2)
        print("Cửa Khóa")