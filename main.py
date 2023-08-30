import os
import time

# Global variables.
player1 = ""
player2 = ""


class Board():
  def __init__(self):
    self.cells = [" ", " ", " ", 
                  " ", " ", " ", 
                  " ", " ", " "]
    self.current = 1
    self.winner = False
    self.gameRunning = True

  def display(self):
    idx = 0
    for i in range(3):
      print(f'{self.cells[idx]} | {self.cells[idx+1]} | {self.cells[idx+2]}')
      if (i < 2):
        print('---------')
      idx += 3
    print()
  
  def updateCell(self, cellNum, currentPlayer):
    global player1, player2
    cell = cellNum - 1
    if (self.cells[cell] == " "):
      if (currentPlayer == 1):
        self.cells[cellNum - 1] = player1
      elif (currentPlayer == 2):
        self.cells[cellNum - 1] = player2
      return True
    else:
      print("There is already a player in that spot!\n")
      return False

  # Checks for a horizontal win.
  def horizontalWin(self):
    idx = 0 
    for i in range(3):
      if ((self.cells[idx] != " ") and 
          (self.cells[idx] == self.cells[idx+1] == self.cells[idx+2])):
        board.winner = self.cells[idx]
        return True
      idx += 3

  # Checks for a vertical win.
  def verticalWin(self):
    idx = 0 
    for i in range(3):
      if ((self.cells[idx] != " ") and 
          (self.cells[idx] == self.cells[idx+3] == self.cells[idx+6])):
        board.winner = self.cells[idx]
        return True
      idx += 1

  # Checks for a diagonal win.
  def diagonalWin(self):
    if (self.cells[4] != " "):
      if ((self.cells[0] or self.cells[2]) == self.cells[4] == 
          (self.cells[6] or self.cells[8])):
        board.winner = self.cells[4]
        return True

  # Checks for a tie.
  def checkTie(self):
    if (board.winner == False):
      if (" " in self.cells):
        return False
      else:
        return True
    return False


def printHeader():
  print("Welcome to Tic-Tac-Toe.")
  print(f'Player 1 is {player1}')
  print(f'Player 2 is {player2}\n')


def displayBoard():
  # Clear the screen.
  os.system("clear")

  # Print the header.
  printHeader()

  # Show the board.
  board.display()


def checkWin():
  if (board.horizontalWin() or board.verticalWin() or board.diagonalWin()):
    board.gameRunning = False
    displayBoard()
    print(f'{board.winner} is the winner!\n')
    return True

def checkTie():
  if (board.checkTie()):
    board.gameRunning = False
    displayBoard()
    print("It's a tie!\n")
    return True


def switchPlayer():
  if (board.current == 1):
    board.current = 2
  elif (board.current == 2):
    board.current = 1

    
def playerSetUp():
  global player1, player2
  player1 = input("Does player 1 want to be X's or O's? (X/O): ")
  if (player1 == "X"):
    player2 = "O"
  if (player1 == "O"):
    player2 = "X"


def main():
  global player1, player2
  playerSetUp()

  while board.gameRunning:
    # Display the board.
    displayBoard()

    # ValidChoice starts as false because the player has not 
    # made a valid choice yet.
    validChoice = False 
    while not validChoice:
      # Player chooses the cell/square.
      cellChoice = int(input(f'Player {board.current}: please choose 1-9.  '))

      # Check if the choice is valid. 
      # If the choice is valid, update the board. Otherwise, choose another cell.
      validChoice = board.updateCell(cellChoice, board.current)

    checkWin()
    checkTie()
    switchPlayer()
    

board = Board()
main()
