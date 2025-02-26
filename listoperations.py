lst=[10,30,20,40]
def oper():
    lst.append(45)
    print(lst)
    lst.sort()
    print(lst)
    lst.sort(reverse="True")
    print(lst)
    lst.pop()
    print(lst)

oper()
