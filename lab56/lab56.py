
try:
  a = float(input('Enter the first side of the triangle: '))
  b = float(input('Enter the second side of the triangle: '))
  c = float(input('Enter the third side of the triangle: '))


  if a < 0 or b < 0 or c < 0:
    exit('All values should be positive')
  
  if a + b > c:
    print('This triangle may exist')
  else:
    print('This triangle can NOT exist!!!')

except ValueError:
  exit('Please enter a number')