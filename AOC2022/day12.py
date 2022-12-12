file = open("./inputs/input12.txt", "r")

grid = []
initialPos = (0, 0)
endPos = (0, 0)
for line in file:
    grid.append(line[:-1])

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "S":
            initialPos = (row, col)
        if grid[row][col] == "E":
            endPos = (row, col)

# traveled = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
traveled = []
def canTravel(currentPos, nextPos):
    row, col = currentPos
    nextRow, nextCol = nextPos

    currentVal = ord(grid[row][col])
    nextVal = ord(grid[nextRow][nextCol])
    if currentVal == 83: # char 'S'
        currentVal = 97 # char 'a'
    if nextVal == 69: # char 'E'
        nextVal = 122

    if (currentVal == nextVal or currentVal + 1 == nextVal) and not traveled[nextRow][nextCol]:
        return True
    return False


class Node:
    def __init__(self, currentPos = (0, 0), path = [], steps = 0):
        self.currentPos = currentPos
        self.path = path
        self.steps = steps

    def canTravel(self, nextPos):
        row, col = self.currentPos
        nextRow, nextCol = nextPos

        currentVal = ord(grid[row][col])
        nextVal = ord(grid[nextRow][nextCol])
        if currentVal == 83: # char 'S'
            currentVal = 97 # char 'a'
        if nextVal == 69: # char 'E'
            nextVal = 122
        if currentVal + 1 >= nextVal and (nextRow, nextCol) not in traveled:
            return True
        return False

    def canTravelReversed(self, nextPos):
        row, col = self.currentPos
        nextRow, nextCol = nextPos

        currentVal = ord(grid[row][col])
        nextVal = ord(grid[nextRow][nextCol])
        if nextVal == 83: # char 'S'
            nextVal = 97 # char 'a'
        if currentVal == 69: # char 'E'
            currentVal = 122
        if currentVal - 1 <= nextVal and (nextRow, nextCol) not in traveled:
            return True
        return False


# PART 1
# def findShortestPath():
#     queue = [Node(initialPos, [], 0)]
#     while queue:
#         node = queue.pop()
#         row, col = node.currentPos
#         # traveled.append(node.currentPos)
#         path = node.path
#         steps = node.steps
#         print(row, col, grid[row][col])
#        
#         if grid[row][col] == "E":
#             return steps
#         
#         # go up
#         nextPos = (row - 1, col)
#         if row != 0 and node.canTravel(nextPos):
#             traveled.append(nextPos)
#             newPath = path.copy()
#             newPath.append(nextPos)
#             newNode = Node(nextPos, newPath, steps + 1)
#             queue.insert(0, newNode)
#
#         # go down
#         nextPos = (row + 1, col)
#         if row != len(grid) - 1 and node.canTravel(nextPos):
#             traveled.append(nextPos)
#             newPath = path.copy()
#             newPath.append(nextPos)
#             newNode = Node(nextPos, newPath, steps + 1)
#             queue.insert(0, newNode)
#             
#         # go left
#         nextPos = (row, col - 1)
#         if col != 0 and node.canTravel(nextPos):
#             traveled.append(nextPos)
#             newPath = path.copy()
#             newPath.append(nextPos)
#             newNode = Node(nextPos, newPath, steps + 1)
#             queue.insert(0, newNode)
#
#         # go right
#         nextPos = (row, col + 1)
#         if col != len(grid[0]) - 1 and node.canTravel(nextPos):
#             traveled.append(nextPos)
#             newPath = path.copy()
#             newPath.append(nextPos)
#             newNode = Node(nextPos, newPath, steps + 1)
#             queue.insert(0, newNode)


# PART 2
def findShortestPath():
    queue = [Node(endPos, [], 0)]
    while queue:
        node = queue.pop()
        row, col = node.currentPos
        # traveled.append(node.currentPos)
        path = node.path
        steps = node.steps
        print(row, col, grid[row][col])
       
        if grid[row][col] == "a":
            return steps
        
        # go up
        nextPos = (row - 1, col)
        if row != 0 and node.canTravelReversed(nextPos):
            traveled.append(nextPos)
            newPath = path.copy()
            newPath.append(nextPos)
            newNode = Node(nextPos, newPath, steps + 1)
            queue.insert(0, newNode)

        # go down
        nextPos = (row + 1, col)
        if row != len(grid) - 1 and node.canTravelReversed(nextPos):
            traveled.append(nextPos)
            newPath = path.copy()
            newPath.append(nextPos)
            newNode = Node(nextPos, newPath, steps + 1)
            queue.insert(0, newNode)
            
        # go left
        nextPos = (row, col - 1)
        if col != 0 and node.canTravelReversed(nextPos):
            traveled.append(nextPos)
            newPath = path.copy()
            newPath.append(nextPos)
            newNode = Node(nextPos, newPath, steps + 1)
            queue.insert(0, newNode)

        # go right
        nextPos = (row, col + 1)
        if col != len(grid[0]) - 1 and node.canTravelReversed(nextPos):
            traveled.append(nextPos)
            newPath = path.copy()
            newPath.append(nextPos)
            newNode = Node(nextPos, newPath, steps + 1)
            queue.insert(0, newNode)


# DFS    
# def findShortestPath(currentPos, stepCount):
#     row, col = currentPos
#     # print(row, col, grid[row][col])
#     traveled[row][col] = 1
#     if grid[row][col] == "E":
#         return stepCount 
#     
#     # go up
#     stepCounts = []
#     if row != 0 and canTravel(currentPos, (row - 1, col)):
#         stepCounts.append(findShortestPath((row - 1, col), stepCount + 1))
#         traveled[row - 1][col] = 0
#
#     # go down
#     if row != len(grid) - 1 and canTravel(currentPos, (row + 1, col)):
#         stepCounts.append(findShortestPath((row + 1, col), stepCount + 1))
#         traveled[row + 1][col] = 0
#         
#     # go left
#     if col != 0 and canTravel(currentPos, (row, col - 1)):
#         stepCounts.append(findShortestPath((row, col - 1), stepCount + 1))
#         traveled[row][col - 1] = 0
#
#     # go right
#     if col != len(grid[0]) - 1 and canTravel(currentPos, (row, col + 1)):
#         stepCounts.append(findShortestPath((row, col + 1), stepCount + 1))
#         traveled[row][col + 1] = 0
#     if stepCounts:
#         return min(stepCounts)
#     else:
#         return 99999999


print(findShortestPath())
