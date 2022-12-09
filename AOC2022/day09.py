file = open("./inputs/input09.txt", "r")

# travelMap = [["0" for _ in range(1000)] for _ in range(1000)]
visited = [[0 for _ in range(1000)] for _ in range(1000)]

headX = 0
headY = 0
tailX = 0
tailY = 0 

# snakeX = [0 for _ in range(10)]
# snakeY = [0 for _ in range(10)]

def moveHead(direction, steps):
    global headX, headY

    def moveTail():
        global tailX, tailY, visited
        if direction == "U":
            if headY == tailY + 2:
                tailX = headX # works for both diagonal and up 
                tailY = headY - 1
        if direction == "D":
            if headY == tailY - 2:
                tailX = headX # works for both diagonal and up 
                tailY = headY + 1
        if direction ==  "R":
            if headX == tailX + 2:
                tailY = headY 
                tailX = headX - 1
        if direction ==  "L":
            if headX == tailX - 2:
                tailY = headY 
                tailX = headX + 1
        visited[tailY][tailX] = 1


    for _ in range(steps):
        if direction == "U":
            headY += 1              
        if direction == "D":
            headY -= 1              
        if direction == "R":
            headX += 1              
        if direction == "L":
            headX -= 1              
        moveTail()



for line in file:
    direction = line[0]
    steps = int(line[2:])
    moveHead(direction, steps)

print(sum([sum(l) for l in visited]))

# for l in range(len(visited) - 1, -1, -1):
#     print(visited[l])
