file = open("./inputs/input08.txt", "r")

treeMap = []

for line in file:
    treeMap.append([int(i) for i in line[:-1]])
    


def isVisible(x, y):
    def isVisibleTop(x, y):
        for i in range(y-1, -1, -1):
            if treeMap[i][x] >= treeMap[y][x]:
                return False
        return True

    def isVisibleBottom(x, y):
        for i in range(y+1, len(treeMap)):
            if treeMap[i][x] >= treeMap[y][x]:
                return False
        return True

    def isVisibleLeft(x, y):
        for i in range(x-1, -1, -1):
            if treeMap[y][i] >= treeMap[y][x]:
                return False
        return True

    def isVisibleRight(x, y):
        for i in range(x+1, len(treeMap[0])):
            if treeMap[y][i] >= treeMap[y][x]:
                return False
        return True

    return isVisibleTop(x, y) or isVisibleBottom(x, y) or isVisibleLeft(x, y) or isVisibleRight(x, y)


def getScenicScore(x, y):
    def countVisibleTop(x, y):
        count = 0
        for i in range(y-1, -1, -1):
            count += 1
            if treeMap[i][x] >= treeMap[y][x]:
                return count
        return count

    def countVisibleBottom(x, y):
        count = 0
        for i in range(y+1, len(treeMap)):
            count += 1
            if treeMap[i][x] >= treeMap[y][x]:
                return count
        return count

    def countVisibleLeft(x, y):
        count = 0
        for i in range(x-1, -1, -1):
            count += 1
            if treeMap[y][i] >= treeMap[y][x]:
                return count
        return count

    def countVisibleRight(x, y):
        count = 0
        for i in range(x+1, len(treeMap[0])):
            count += 1
            if treeMap[y][i] >= treeMap[y][x]:
                return count
        return count

    return countVisibleTop(x, y) * countVisibleBottom(x, y) * countVisibleRight(x, y) * countVisibleLeft(x, y)


count = 0
maxScenicScore = 0
for row in range(0, len(treeMap)):
    for col in range(0, len(treeMap[0])):
        if isVisible(col, row):
            # print(row, col, treeMap[row][col])
            count += 1
        maxScenicScore = max(maxScenicScore, getScenicScore(col, row))

print(count)
print(maxScenicScore)

