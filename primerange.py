def is_prime(num):
    for x in range( 2, num):
        if (num%x) == 0:
            return False
    return True


def main():
    low = int(input("Enter the lower range:"))
    high = int(input("Enter the higher range:"))

    print("Prime numbers between",low,"and",high,"are:")
    for num in range(low,high+1):
        if is_prime(num):
            print(num)

if __name__=='__main__':
    main()
