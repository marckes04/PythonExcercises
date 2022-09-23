def drawField(field):
    for row in range(9): #0,1,2,3,4...
                         #0,.,1,.,2...
        if row % 2 == 0: #0.2.4 ...
            practicalRow = int(row/2) 
            for column in range(9): #0,1,2,3,4...
                                    #0,.,1,.,2...
                if column % 2 == 0:#0.2.4
                    practicalColumn = int(column/2) #0,1,2...
                    if column != 8:
                        print(field[practicalRow][practicalColumn], end='')
                    else:
                        print(field[practicalRow][practicalColumn])
                else:
                    print('|', end='')
        else:
            print('-'*9)
 
player = 1
currentField = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
rowCount = [4, 4, 4, 4, 4]
drawField(currentField)
while(True):
    print(f'Players {player} turn')
    moveColumn = int(input('Column: '))
    if player == 1:
        if currentField[rowCount[moveColumn]][moveColumn] == ' ':
            currentField[rowCount[moveColumn]][moveColumn] = 'X'
            rowCount[moveColumn] -= 1
            player = 2
    else:
        if currentField[rowCount[moveColumn]][moveColumn] == ' ':
            currentField[rowCount[moveColumn]][moveColumn] = 'O'
            rowCount[moveColumn] -= 1
            player = 1
    drawField(currentField)
