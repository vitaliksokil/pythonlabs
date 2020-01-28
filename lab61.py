import math
def triangleArea(AB,BC,CA):
  if AB + BC > CA:
    s = (AB+BC+CA)/2
    A = math.sqrt(s*(s-AB)*(s-BC)*(s-CA))
    return A
  else:
    exit('Incorrect lengths!!!')

try:
  AB = float(input('Enter length of AB side of triangle: '))
  BC = float(input('Enter length of BC side of triangle: '))
  CA = float(input('Enter length of CA side of triangle: '))
  A = triangleArea(AB,BC,CA)
  print('Area of the triangle is : ',A)
except ValueError:
  print('Please enter a number!!!')