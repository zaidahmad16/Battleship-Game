import random

def createBoard(size):
    board = []
    for i in range(size):
        board.append(['~'] * size)
    return board

def addShip(board, numShips):
    size = len(board)
    shipsPlaced = 0
    while shipsPlaced < numShips:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if board[x][y] == '~':
            board[x][y] = 'S'
            shipsPlaced += 1
    return board

def checkSetupError(size, numShips):
    if size < 2 or size > 5:
        return True
    maxShips = (size * size) - 2
    if numShips < 1 or numShips > maxShips:
        return True
    return False

def displayBoard(board, revealShips=False):
    for row in board:
        displayRow = []
        for cell in row:
            if cell == 'S' and not revealShips:
                displayRow.append('~')
            else:
                displayRow.append(cell)
        print(" ".join(displayRow))

def fireShot(board, x, y):
    if board[x][y] == 'S':
        board[x][y] = 'X'
        return True
    else:
        board[x][y] = 'O'
        return False

def checkFireError(board, x, y):
    size = len(board)
    if x < 0 or x >= size or y < 0 or y >= size:
        return True
    if board[x][y] == 'X' or board[x][y] == 'O':
        return True
    return False

def playRound(board, numShips):
    shots = numShips
    hits = 0

    for shot in range(shots):
        displayBoard(board)
        while True:
            user_input = input("Enter row and column to take a shot (e.g., 2 3): ")
            parts = user_input.split()
            if len(parts) != 2:
                print("Invalid input. Please enter exactly two numbers separated by a space, like '2 3'.")
                continue
            try:
                x = int(parts[0])
                y = int(parts[1])
                break
            except ValueError:
                print("Invalid input. Please enter numeric values only.")

        if checkFireError(board, x, y):
            print("Invalid shot. Try again.")
            continue

        if fireShot(board, x, y):
            print("Hit!")
            hits += 1
        else:
            print("Miss!")

    print("\nEnd of round:")
    displayBoard(board, revealShips=True)
    return hits

def main():
    #Manages the number of rounds of Battleship to play, including board setup and score tracking.
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetupError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")
        
        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")

        hits = playRound(board, numShips)
        global totalScore
        totalScore += hits
        currentRound += 1

    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out of {numShips * numRounds}.")
    return

if __name__ == "__main__":
    main()
