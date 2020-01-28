def deposite(money,rate,years):
  for i in range(0,years):
    money = money + (money*(rate/100))
  return money

try:
  money = float(input('Enter number of money you want to put to the bank: '))
  rate = float(input('Enter annual rate in percentages : '))
  years = int(input('Enter the deposite duration is years : '))
  amount = deposite(money,rate,years)
  print('The amount at the time of termination of the deposit agreement. : ',amount)
except ValueError:
  print('Please enter a number!!!')