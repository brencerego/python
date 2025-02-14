num = int(input("Enter a Number:"))
flag = 0
for i in range(2,(int(num/2))+1):
    if num % i == 0:
        flag = 1
if flag == 1:
    print(f"{num} is not Prime.")
else :
    print(f"{num} is Prime.")
