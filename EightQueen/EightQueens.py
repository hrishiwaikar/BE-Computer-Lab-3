import time
import json
row=['_','_','_','_','_','_','_','_']

def isValid(board,qX,qY):
    i = qX-1
    j = qY


    #Vertical Check
    while i>=0 and j<=7:
        if board[i][j]=='Q':
            return False
        else:
            i=i-1

    i = qX - 1
    j = qY
    #Right Diagonal
    while i>=0:
        j=0
        while j<=7:
            if ((i+j)==(qX+qY)) and board[i][j]=='Q':
                return False
            else:
                j=j+1
        i=i-1


    i = qX-1
    j = 0

    #Left diagonal
    while i >= 0:
        j = 0
        while j <= qY:
            if (abs(i-j)==abs(qX-qY)) and board[i][j] == 'Q':
                return False
            else:
                j = j + 1
        i = i - 1



    return True



def display(board):
    print
    print
    for row in board:
        for box in row:
            print box,
        print



def recursiveQueen(board,level):

    level=level+1
    if level<8:
        #print
        newrow=list(row)
        board.append(newrow)
        #print 'level ' + str(level)
        #display(board)
        #print



        for i in range(8):
            newboard=list(board)

            if isValid(newboard,level,i):
                newboard[level][i] = 'Q'
                #display(newboard)
                #print 'isValid going to next level'
                recursiveQueen(newboard,level)
                #print 'Found an invalid descendant so came back to this level '+str(level)+'where board is'
                #display(board)

                newboard[level][i]='_'

            #else:
                #print 'is invalid'

        #print 'Done checking all children , will return to parent'

    else :
        display(board)
        time.sleep(5)


if __name__=='__main__':

    with open('startposition.json') as json_data:
        d = json.load(json_data)

    queen_position = int(d["position"])
    firstrow = []

    for i in range(8):
        if i == queen_position:
            firstrow.append('Q')
        else:
            firstrow.append('_')

    startboard=[]
    startboard.append(firstrow)
    print startboard
    recursiveQueen(startboard,0)