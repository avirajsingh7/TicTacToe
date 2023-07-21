#TIC TAC TOE

def evaluate(b) :
   
    # Checking for Rows for X or O victory.
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
            if (b[row][0] == 'X') :
                return 10
            elif (b[row][0] == 'O') :
                return -10
 
    # Checking for Columns for X or O victory.
    for col in range(3) :
      
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
         
            if (b[0][col] == 'X') :
                return 10
            elif (b[0][col] == 'O') :
                return -10
 
    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
     
        if (b[0][0] == 'X') :
            return 10
        elif (b[0][0] == 'O') :
            return -10
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
        if (b[0][2] == 'X') :
            return 10
        elif (b[0][2] == 'O') :
            return -10
 
    # Else if none of them have won then return 0
    return 0

def GameStart():
    board = [
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ]
    ]
    return board        

def ShowBoard(Board):
    for i in range(3) :
        for j in range(3):
            print(Board[i][j],end=" ")
        print("")
    
Board=GameStart()
ShowBoard(Board)


def movesLeft(Board):
    for i in range(3) :
        for j in range(3) :
            if (Board[i][j] == '_') :
                return True
    return False

print("Player1 Turn")
turn = True
player='O'
opponent='X'

def empty_spots(b):
    emp=[]
    for i in range(3) :
        for j in range(3) :
            if (b[i][j] == '_') :
                emp.append([i,j])         
    return emp

def miniMax(br,player):
    b = [[br[x][y] for y in range(len(br[0]))] for x in range(len(br))]
    empty_spot=empty_spots(b)
    score = evaluate(b)
    if(score==10):
        best=[10,[-1,-1]]
        return best
    elif(score==-10):
        best=[-10,[-1,-1]]
        return best
    elif(bool(movesLeft(b))==False):
        best=[0,[-1,-1]]
        return best
    
    scores=[]
    for i in range(len(empty_spot)):
        b[empty_spot[i][0]][empty_spot[i][1]]=player
        if(player=='X'):
            result=miniMax(b,'O')
            scores.append(result[0])
        else:
            result=miniMax(b,'X')
            scores.append(result[0])
        b[empty_spot[i][0]][empty_spot[i][1]]='_'

    best=[-1000,[]]
    if(player=='X'):
        bestScore = -1000
        for j in range(len(scores)):
            if(scores[j]>bestScore):
                bestScore=scores[j]
                best[0]=scores[j]
                best[1]=empty_spot[j]
    else:
        bestScore = 1000
        for j in range(len(scores)):
            if(scores[j]<bestScore):
                    bestScore=scores[j]
                    best[0]=scores[j]
                    best[1]=empty_spot[j]
    return best
    
while(movesLeft(Board) and int(evaluate(Board))==0):
    if(turn):
        a=int(input("Enter row here"))-1
        b=int(input("Enter column here"))-1
        Board[a][b]='O'
        turn = False
        ShowBoard(Board)
        print("Player2 Turn")
    else:
        result=miniMax(Board,'X')
        print(result)
        a=result[1][0]
        b=result[1][1]
        Board[a][b]='X'
        turn=True
        ShowBoard(Board)
        print("Player1 Turn")
        
        
if(int(evaluate(Board))==10):
    print("Player1 is winner")
elif(int(evaluate(Board))==-10):
    print("Player 2 is winner")
else:
    print("Game is Draw")
