dic={"user1":"12345556",
"user2":"123456",
"user3":"888888",
"user4":"123456",
"user5":"123456",
"user6":"123456",
"user7":"123456",
"user8":"123456",
"user9":"123456",
"user10":"123456"}


user = input("nhap username: ")
password = input("nhap vao password: ")
if user not in dic:
    print("user khong ton tai ")
else:
    if dic[user]!=password:
        print("password sai ")
    else:
        print("dang  nhap thanh cong ")