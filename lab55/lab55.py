
try:
  number = int(input('Enter a positive integer value: '))
  if number < 0 :
   exit('Value should be positive ')
  i = 2
  while i < (number // 2)  :
    if number % i == 0:
      print('This number is NOT prime')
      break
    i+=1 
  else:
    print('This number IS prime')
except ValueError:
  exit('Please enter a number')