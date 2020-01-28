#!/usr/bin/env/ python3
try:
  number = int(input('Enter positive integer value: '))
  if number < 0:
    print('Please enter positive value')
  else:
    print('Is the number power of 2: ' + str(number and (not(number & (number - 1)))))
except ValueError:
  print('Please enter a number')