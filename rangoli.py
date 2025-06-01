def printrangoli(size):
    alpha="abcdefghijklmnopqrstuvwxyz"
    lines=[]
    
    for i in range(size):
        s="-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4*size-3,"-"))
        
    for i in lines[::-1][1:] + lines:
        print(i)
        
size = int(input("Enter the size of the rangoli:"))
printrangoli(size)
