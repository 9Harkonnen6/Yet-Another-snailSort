snailMap = [[1,2,3,4],[4,5,6,7],[7,8,9,1],[1,2,3,4]]
snailRoad = []


rowStart, rowEnd = 0, len(snailMap)-1
columnStart, columnEnd = 0, len(snailMap[0])-1

if len(snailMap) == 0:
    print('There is no map at all!')

while rowStart <= rowEnd and columnStart <= columnEnd:
    for i in range(columnStart, columnEnd+1):
        snailRoad.append(snailMap[rowStart][i])
    rowStart+=1
    for i in range(rowStart, rowEnd+1):
        snailRoad.append(snailMap[i][columnEnd])
    columnEnd-=1
    if rowStart <= rowEnd:
        for i in range(columnEnd, columnStart-1, -1):
            snailRoad.append(snailMap[rowEnd][i])
        rowEnd-=1
    if columnEnd <= columnEnd:
        for i in range(rowEnd, rowStart-1, -1):
            snailRoad.append(snailMap[i][columnStart])
    columnStart+=1

for e in snailMap:
    print(e)
print('\n')
print(snailRoad)
