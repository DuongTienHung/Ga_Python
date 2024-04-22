lst=[1,2,5,8,9,9,10]
lst_max=[]
for i in lst:
    if i==max(lst):
        continue
    else:
        lst_max.append(i)
print("gia tri lon thu 2 trong list la :",max(lst_max))

lst_index=[]
for j in range(len(lst)):
    if lst[j]== max(lst_max):
        lst_index.append(j)
print(lst_index)
