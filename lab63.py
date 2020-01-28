def deposite(money,requiredAmount,rate):
  years = 0
  while requiredAmount >= money :
    money = money + (money*(rate/100))
    years += 1
  return years

try:
  money = float(input('Enter number of money you want to put to the bank: '))
  requiredAmount = int(input('Enter the required amount : '))
  rate = float(input('Enter annual rate in percentages : '))
  years = deposite(money,requiredAmount,rate)
  print('Years required to increase the deposit to the required amount : ',years)
except ValueError:
  print('Please enter a number!!!')