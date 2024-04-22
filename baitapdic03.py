d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]


print("1. thong tin nhung user cos so dien thoai ket thuc =8 la : ")
for dong in d:
    phone_check=dong["phone"]
    if phone_check[-1] =="8":
        name_show=dong["name"]
        phone_show=dong["phone"]
        email_show=dong["email"]
        print("-"*50)
        print("name: ",name_show)
        print("phone: ",phone_show)
        print("email: ",email_show)

print("#"*50)
print("cac user o co dia chi email ")
for dong in d:
    if dong["email"]=="":
        name_show=dong["name"]
        phone_show=dong["phone"]
        email_show=dong["email"]

        print("name: ",name_show)
        print("phone: ",phone_show)
        print("email: ",email_show)