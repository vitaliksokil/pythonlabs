try:
  print('All data enter in CENTIMETERS!!!')
  doorHeight = float(input('Enter height of the door: '))
  doorWidth = float(input('Enter width of the door: ')) 
  #h = 220
  #w = 60
  door = [doorHeight,doorWidth]
  #a = 50
  #b = 50
  #c = 80
  boxLength = float(input('Enter length of the box: '))
  boxWidth = float(input('Enter width of the box: '))
  boxHeight = float(input('Enter height of the box: ')) 
  
  box = [boxLength,boxWidth,boxHeight]
  boxMinDimension = min(box)
  boxMaxDimension = max(box)
  boxAverageDimension = sum(box)/len(box)
  doorMinDimension = min(door)
  doorMaxDimension = max(door)
  doorAverageDimension = sum(door) / len(door)
  if boxMinDimension < doorMinDimension and boxAverageDimension < doorAverageDimension and boxMaxDimension < doorMaxDimension :
    print('There is a way to fit the box through the door')
  else:
    print('There is NO way to fit the box through the door')
except ValueError:
  exit('Please enter a number')