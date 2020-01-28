import random

def getShapeNameByNumber(num):
  if(num == 1):
    shape = 'rock'
  elif(num == 2):
    shape = 'paper'
  elif(num == 3):
    shape = 'scissors'
  return shape
def roshambo():
  print('Choose one item(enter a number of it) \n 1.Rock \n 2.Paper \n 3.Scissors ')
  selectedShape = int(input())
  if(selectedShape != 1 and selectedShape != 2 and selectedShape != 3):
    exit('Please enter the correct value(1,2 or 3)')
  selectedShape = getShapeNameByNumber(selectedShape)

  computerChoice = random.randint(1,3)
  computerChoice = getShapeNameByNumber(computerChoice)

  print('Computer choice : ' , computerChoice)
  if(selectedShape == 'rock' and computerChoice == 'paper'):
    print('You lose!!!')
  elif(selectedShape == 'scissors' and computerChoice == 'rock'):
    print('You lose!!!')
  elif(selectedShape == 'paper' and computerChoice == 'scissors'):
    print('You lose!!!')
  elif(selectedShape == computerChoice):
    print('Try one more time')
    roshambo()
  else:
    print('You win!!!')

try:
 roshambo()
except ValueError:
  exit('Please enter a number')