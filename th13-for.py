"""
TH13 :
Số hoàn thiện (hay còn gọi là số hoàn chỉnh, số hoàn hảo hoặc số hoàn thành) là một số
nguyên dương mà tổng các ước nguyên dương chính thức của nó
(số nguyên dương bị nó chia hết ngoại trừ nó) bằng chính nó.
Tìm tất cả những số hoàn thiện trong phạm vi từ 1-1000
"""
for number in range(1,1001,1):
    s=0
    for i in range(1,number,1):
        if number%i==0:
            s=s+i
    if s==number:
        print(s,end=" ")