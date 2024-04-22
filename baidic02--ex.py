dict_01 = {
    "A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
    "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
    "O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
    "V":4,"W":4,"X":8,"Y":4,"Z":10
}
str_1="University of Technology and Education"

lst_chu=[]
lst_so=[]
for i in dict_01:
    lst_chu.append(i)
    lst_so.append(str(dict_01[i]))

#1 tach so va chu
a=" ".join(lst_chu)
print("chuoi ky tu sau tach la: ",a)

b=" ".join(lst_so)
print("chuoi so sau tach la: ",b)

# 2 tinh tong cac so
sum=0
for j in dict_01:
    sum=sum+dict_01[j]
print("tong cac chu so la :" , sum)

#3:chuyen doi chuoi
str_2= str_1.upper()


str_chuyendoi=""
for k in str_2:
    if k==" ":
        str_chuyendoi=str_chuyendoi+k
    else:
        str_chuyendoi=str_chuyendoi+str(dict_01[k])


print(str_chuyendoi)