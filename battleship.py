import random

#Function 1: creating the board
def createBoard(size):
    #start an emppty list to represent the board
    board=[]
    #loop to create rows, each filled with "~"(empty cells)
    for _ in range(size):
        board.append(['~']*size)
    return board # return the board

#Function 2: adds ships to the game
def addShip(board,numShips):
    size= len(board)
    shipsPlaced=0
    while shipsPlaced<numShips:
        x=random.randint(0,size-1)
        y=random.randint(0,size-1)
        if board[x][y]=='~': # place a ship if cell is empty
            board[x][y]='S'
            shipsPlaced+=1
    return board

#Function 3: check if game the setup works
def checkSetupError(size,numShips):
    #check if the board size is within the range(2-5)
    if size<2 or size>5:
        return True #return true if the board size is invalid
    #calculate the max allowed ships for the board size
    maxShips=(size*size)-2
    #check if the number of ships for the given board size
    if numShips < 1 or numShips > maxShips:
        return True #return if the number of ships is invalid
    return False # Return False if both board size and ship count are valid

#Function 4: creates the display for the game
def displayBoard(board,revealShips=False):
    #loop through each row in board
    for row in board:
        displayRow=[] #temporray list to store the dislplay version of the row
        for cell in row:
            if cell =='S'and not revealShips:
                displayRow.append('~')# dsiplay "~" for ships if not revealing
            else:
                displayRow.append(cell)#display actual cell content otherwise
        #print the row as a space-separated string
        print(" ".join(displayRow))

#Function 5: check if shot hit or miss

def fireShot(board,x,y):
    #check if the shot hits the ship
    if board[x][y] == 'S':
        board[x][y] = 'X'  # Mark the hit with 'X'
        return True  # Return True if its a hit
    else:
        board[x][y] = 'O'  # Mark the miss with 'O'
        return False  # Return False if its a miss
    
#Function 6: check if any errors in the shot
def checkFireError(board,x,y):
    size=len(board) # get board size
    #check if coords are within the board bounds
    if x<0 or x >= size or y <0 or y>= size:
        return True
    #check if the cell has already been shot at marked 'X' or 'O'
    if board[x][y]=='X' or board[x][y]=='O':
        return True # return True if the cell was already used
    return False # return False if the input coords are valid

#Function 7: starts the round, puts all functions together
def playRound():
    
    #ask the user to enter board size and number of ships
    size=int(input("enter the size of the board (2-5): "))
    numShips= int(input("enter the number of ships: "))
    
    #check if the board size and number of ships are valid
    if checkSetupError(size,numShips):
        print("Invalid board size or ship count. Please restart the game")
        return
    # start the board and place the ship
    board = createBoard(size)
    addShip(board,numShips)

    # number of shots equal to the number of ships and starts the hit counter
    shots = numShips
    hits=0
    #main loop for each shot  in the round
    for shot in range(shots):
        displayBoard(board)
        while True:
            user_input = input("Enter row and column to take a shot (e.g., 2 3): ")
            # Split the input by space and check if we get exactly two parts
            parts = user_input.split()
        
            if len(parts) != 2:
                print("Invalid input. Please enter exactly two numbers separated by a space, like '2 3'.")
                continue
            # Try to convert both parts to integers
            try:
                x = int(parts[0])
                y = int(parts[1])
                break  # Exit the loop if conversion is successful
            except ValueError:
                print("Invalid input. Please enter numeric values only.")

        #make sure shot coords are valid
        if checkFireError(board,x,y):
            print("Invalid shot. try agian")
            continue

        #fire the shot and update hit count if its a hit
        if fireShot(board,x,y):
            print("hit!")
            hits+=1 # goes up each time there's a succesful hit
        else:
            print("miss!") # tells the user they missed

    # end of round summary
    print("\nEnd of round:")
    displayBoard(board,revealShips=True) # reveal ships at the end of the round
    print(f"Final score: {hits} out of {numShips}")# show score (hits out of ships)

 # main function to start game   
if __name__=="__main__":
    #aks the user to enter the number of rounds they want to play
    rounds= int(input("enter the number of rounds of battleship you want to play: "))
    for _ in range(rounds):
        playRound() # play each round
