import random

def rps(n):
  if n==1:
    return 'Rock'
  elif n==2:
    return 'Paper'

  else:
    return 'Scissor'
  

name=input('Type your name: ')

while(True):

  k=random.randint(1,3)
  

  print('\nComputer choosed, now it is your turn\n')

  

  print('1. Rock, 2. Paper 3. Scissor\n')
  
  n=int(input('Your Choice: '))

  p=rps(k)
  

  

  if n==k:
    print(f'It is Draw because you both choosed {p}\n')

  elif n==1 and k==2:
    print(f'Sorry {name}, Computer won because he choosed {p}\n')

  elif n==2 and k==1:
    print(f'Congratulations {name}, You won because opponent choosed {p}\n')

  elif n==1 and k==3:
    print(f'Congratulations {name}, You won because opponent choosed {p}\n')

  elif n==3 and k==1:
    print(f'Sorry {name}, Computer won because he choosed {p}\n')

  elif n==2 and k==3:
    print(f'Sorry {name}, Computer won because he choosed {p}\n')

  elif n==3 and k==2:
    print(f'Congratulations {name}, You won because opponent choosed {p}\n')

  else:
    print('Wrong Input... Try again\n')
    continue

  print(f'{name}, Do you wanna play more, Y/N : ')
  l=input()
  l=l.upper()

  if l=='Y':
    continue

  elif l=='N':
    print(f'Bye....')
    break
    

  else:
    print(f'Sorry {name}, wrong input....we think, you do not wanna play anymore... Bye')


  


