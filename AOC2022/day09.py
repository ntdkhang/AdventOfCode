file = open("./inputs/input09.txt", "r")

# travelMap = [["0" for _ in range(1000)] for _ in range(1000)]
visited = [[0 for _ in range(1000)] for _ in range(1000)]

headX = 0
headY = 0
tailX = 0
tailY = 0 

snakeX = [500 for _ in range(10)]
snakeY = [500 for _ in range(10)]

def moveHead(direction, steps):
    global headX, headY

    def moveTails():
        for index in range(1, 10):
            if abs(snakeY[index - 1] - snakeY[index]) == 2:
                if snakeX[index - 1] > snakeX[index]:
                    snakeX[index] += 1
                elif snakeX[index - 1] < snakeX[index]:
                    snakeX[index] -= 1
                
                snakeY[index] += (snakeY[index - 1] - snakeY[index]) // 2 
                    

            if abs(snakeX[index - 1] - snakeX[index]) == 2:
                if snakeY[index - 1] > snakeY[index]:
                    snakeY[index] += 1
                elif snakeY[index - 1] < snakeY[index]:
                    snakeY[index] -= 1
                
                snakeX[index] += (snakeX[index - 1] - snakeX[index]) // 2 

        visited[snakeY[9]][snakeX[9]] = 1
        


    for _ in range(steps):
        if direction == "U":
            # headY += 1              
            snakeY[0] += 1
        if direction == "D":
            # headY -= 1              
            snakeY[0] -= 1
        if direction == "R":
            # headX += 1              
            snakeX[0] += 1
        if direction == "L":
            # headX -= 1              
            snakeX[0] -= 1
        moveTails()



for line in file:
    direction = line[0]
    steps = int(line[2:])
    moveHead(direction, steps)

print(sum([sum(l) for l in visited]))

# for l in range(len(visited) - 1, -1, -1):
#     print(visited[l])
