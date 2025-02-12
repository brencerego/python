def is_prime(num):
  for n in range( 2, num):
    if (num % n) == 0:
      return False
  return True

n = int(input("Enter the number:"))
if (is_prime(n)):
  print("It is prime")
else:
  print("It is not prime")
