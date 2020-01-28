import math

try:
  print('Enter coeffs for quadratic equation : ')
  a = float(input('Enter a: '))
  b = float(input('Enter b: '))
  c = float(input('Enter c: '))
  D = (b**2) - (4*a*c)
  if D < 0 :
    exit('There is no solutions!!!')
  elif D == 0:
    x = -(b/(2*a))
    print('X = ',x)
  else:
    x1 = ((-b) + math.sqrt(D))/(2*a)
    x2 = ((-b) - math.sqrt(D))/(2*a)
    print('X1: ', x1)
    print('X2: ', x2)
    
except ValueError:
  exit('Please enter a number')