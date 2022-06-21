
def printCurrentState():
    print(f"""
         |     |     |
      {tableState[0]}  |  {tableState[1]}  |  {tableState[2]}  |
    -----|-----|-----|
      {tableState[3]}  |  {tableState[4]}  |  {tableState[5]}  |
    -----|-----|-----|
      {tableState[6]}  |  {tableState[7]}  |  {tableState[8]}  |
    -----|-----|-----| 
          
    """)
tableState = [1,2,3,4,5,6,7,8,9]


def switchPlayer():
    global currentPlayer
    if currentPlayer==1:
        currentPlayer = 2
    else:
        currentPlayer = 1


def checkWin():
    global winner
    #1
    if(tableState[0]==tableState[1] and tableState[0]==tableState[2]):
        if(tableState[0]=='x'):
            winner = 1
        else:
            winner = 2
    #2
    if (tableState[3] == tableState[4] and tableState[3] == tableState[5]):
        if (tableState[3] == 'x'):
            winner = 1
        else:
            winner = 2
    #3
    if (tableState[6] == tableState[7] and tableState[6] == tableState[8]):
        if (tableState[6] == 'x'):
            winner = 1
        else:
            winner = 2
    #4
    if (tableState[0] == tableState[3] and tableState[0] == tableState[6]):
        if (tableState[0] == 'x'):
            winner = 1
        else:
            winner = 2
    #5
    if (tableState[1] == tableState[4] and tableState[1] == tableState[7]):
        if (tableState[1] == 'x'):
            winner = 1
        else:
            winner = 2
    #6
    if (tableState[2] == tableState[5] and tableState[2] == tableState[8]):
        if (tableState[2] == 'x'):
            winner = 1
        else:
            winner = 2
    #7
    if (tableState[0] == tableState[4] and tableState[0] == tableState[8]):
        if (tableState[0] == 'x'):
            winner = 1
        else:
            winner = 2
    #8
    if (tableState[2] == tableState[4] and tableState[2] == tableState[6]):
        if (tableState[2] == 'x'):
            winner = 1
        else:
            winner = 2

    if winner == -1:
        return False
    else:
        return True

def play():
    chanceleft = 9
    valid = False
    while chanceleft>0:
        printCurrentState()
        print(f'player {currentPlayer} turn:')
        init = int(input('Enter the loction: '))
        tableState[init - 1] = xo[currentPlayer]

        if (tableState[init-1] == xo[1]):
            valid = True
        else:
            print("Oops! You have OverWrite!!.")

            break

        win = checkWin()
        if(win):
            return

        switchPlayer()


def result():
    printCurrentState()
    if winner == -1:
        print('Game Draw')
    elif winner == 1:
        print('Winner is Player 1')
    else:
        print('Winner is Player 2')

xo={1:'x',2:'o'}
winner = -1
currentPlayer = 1
play()
result()