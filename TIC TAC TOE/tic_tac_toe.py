
## | |   0
#------- 1
#  | |   2
#------- 3
#  | |   4
#0 1 2 3 4



def drawField(field):
    for row in range(5): #0,1,2,3,4
        if row%2 == 0:
            practicalRow = int(row/2) #0,1,2
            for column in range(5): #0,1,2,3,4
                if column%2 == 0:# 0,2,4
                    practicalColumn = int(column/2)
                    if column !=4:
                        print(field[practicalColumn][practicalRow],end = "")
                    else:
                       print(field[practicalColumn][practicalRow]) 
                else:
                    print("|",end = "")
        else:
            print("-----")
Player = 1
currentField = [[" "," "," "],[" ", " ", " "],[" ", " ", " "]]
drawField(currentField)
while(True): #TRUE == TRUE
    print("Player turn: ",Player)
    MoveRow = int(input("Please enter the Row:\n"))#0,1,2
    MoveColumn = int(input("Please enter the column:\n"))#0,1,2
    if Player == 1:
        #Make move for player 1
        currentField[MoveColumn][MoveRow] = "X"
        Player = 2
    else:
        #Make move for player 2
        currentField[MoveColumn][MoveRow] = "O"
        Player = 1
    drawField(currentField)
 
