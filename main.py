import os
import time


class Board():
  def __init__(self):
    self.cells = [" ", " ", " ", 
                  " ", " ", " ", 
                  " ", " ", " "]
    self.player1 = ""
    self.player2 = ""
    self.current = None
    self.gameRunning = True
    self.gameType = None
    self.winner = None

  def display(self):
    idx = 0
    for i in range(3):
      print(f'{self.cells[idx]} | {self.cells[idx+1]} | {self.cells[idx+2]}')
      if (i < 2):
        print('---------')
      idx += 3
    print()
  
  def updateCell(self, cellNum, currentPlayer):
      cell = cellNum - 1
      if (self.cells[cell] == " "):
          if (currentPlayer == 1):
              self.cells[cellNum - 1] = self.player1
          elif (currentPlayer == 2):
              self.cells[cellNum - 1] = self.player2
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
          #if ((self.cells[0] or self.cells[2]) == self.cells[4] == 
          #(self.cells[6] or self.cells[8])):
          if (self.cells[0] == self.cells[4] and self.cells[4] == self.cells[8]):
              board.winner = self.cells[4]
              return True
          if (self.cells[2] == self.cells[4] and self.cells[4] == self.cells[6]):
              board.winner = self.cells[4]
              return True
      return False


  # Checks for a tie.
  def checkTie(self):
    if (board.winner == None):
      if (" " in self.cells):
        return False
      else:
        return True
    return False


def printHeader():
  print("Welcome to Tic-Tac-Toe.")
  print(f'Player 1 is {board.player1}')
  print(f'Player 2 is {board.player2}\n')


def displayBoard():
  # Clear the screen.
  #os.system("clear")

  # Print the header.
  printHeader()

  # Show the board.
  board.display()


def aiCheckWin():
    if (board.horizontalWin() or board.verticalWin() or board.diagonalWin()):
        return True
    else:
        return False


def aiMove():
    print(f'Current Player: {board.current}')
    print("AI making a move.")
    choice = None
    for cell in range(9):
        print(f'cell: {cell+1} | {board.cells[cell]}')
        if (board.cells[cell] == " "):
            board.cells[cell] = board.player2
            if aiCheckWin():
                #break
                return None
            # Now check if the opponent will win if they choose that cell.
            board.cells[cell] = board.player1
            if aiCheckWin():
                print(f'Player 1 can win in cell {cell+1}')
                board.winner = None
                board.cells[cell] = board.player2
                #break
                return None
            board.cells[cell] = " "
            if (choice == None):
                print(f'choice = {cell} aka {cell+1}')
                choice = cell

    #validChoice = board.updateCell(choice, board.current)
    print()
    board.cells[choice] = board.player2
    return None


def checkWin():
  print(f'Checking win for player {board.current}')
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

    
def playerSetUp():
    board.gameType = input("Do you want to play Singleplayer or Multiplayer? (S/M): ")
    board.player1 = input("Does player 1 want to be X's or O's? (X/O): ")
    if (board.player1 == "X"):
        board.player2 = "O"
    if (board.player1 == "O"):
        board.player2 = "X"
    board.current = 1


def switchPlayer():
  if (board.current == 1):
    board.current = 2
  elif (board.current == 2):
    board.current = 1


def main():
    playerSetUp()

    while board.gameRunning:
        # Display the board.
        displayBoard()

        # If the gameType is "M", then both players are real people and we 
        # need to check and make sure their choices are valid.
        
        # If the gameType is "S", then the current player is player 1 who is 
        # real person and we need to make sure their choice is valid.
        if (board.gameType == "M" or board.current == 1):

            # ValidChoice starts as false because the player has not 
            # made a valid choice yet.
            validChoice = False 
            while not validChoice:
                # Player chooses the cell/square.
                cellChoice = int(input(f'Player {board.current}: please choose 1-9.  '))

                # Check if the choice is valid. 
                # If the choice is valid, update the board. Otherwise, choose another cell.
                validChoice = board.updateCell(cellChoice, board.current)
                print(f'Player {board.current} chose {cellChoice}')
        
        # Otherwise, the gameType is "S" and the current player is player 2
        # which is the AI.
        else:
            aiMove()

        checkWin()
        checkTie()
        switchPlayer()
    

board = Board()
main()
