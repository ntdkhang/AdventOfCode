file = open("./inputs/input10.txt", "r")

valueAt = [0] * 1000

currentCycle = 1
currentX = 1

for line in file:
    # print(currentCycle, currentX)
    valueAt[currentCycle] = currentX
    if line[:4] == "noop":
        currentCycle += 1
    else:
        # print(line.split()[1])
        valueAt[currentCycle + 1] = currentX
        valueAt[currentCycle + 2] = currentX
        currentX += int(line.split()[1])
        currentCycle += 2

signalStrengths = 0
for i in range(20, 221, 40):
    signalStrengths += i * valueAt[i]
    
print(signalStrengths)


# PART 2:

# cycle starts at 1
# pixel index starts at 0
# for row in range(6):
#     for col in range(1, 41):
#         cycle = row * 40 + col
#         if valueAt[cycle]  


