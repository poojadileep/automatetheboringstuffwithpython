def printTable(tabledata):
    colWidths = [0] * len(tabledata)  
    for y in range(len(tabledata)):
        for x in tabledata[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)

    for x in range(len(tabledata[0])) :
        for y in range(len(tabledata)) :
            print(tabledata[y][x].rjust(colWidths[y]), end = ' ')
        print()
tableData = [['apples', 'oranges', 'cherries', 'banana',],
             ['Alice', 'Bob', 'Carol', 'David',],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)