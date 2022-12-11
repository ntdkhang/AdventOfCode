file = open("./inputs/input10.txt", "r")

valueAt = [0] * 1000

currentCycle = 1
currentX = 1
valueAt[1] = 1

for line in file:
    # print(currentCycle, currentX)
    if line[:4] == "noop":
        currentCycle += 1
    else:
        # print(line.split()[1])
        valueAt[currentCycle] = currentX
        valueAt[currentCycle + 1] = currentX
        currentX += int(line.split()[1])
        currentCycle += 2

    valueAt[currentCycle] = currentX

signalStrengths = 0
for i in range(20, 221, 40):
    signalStrengths += i * valueAt[i]
    
print(signalStrengths)


# PART 2:

# cycle starts at 1
# pixel index starts at 0
pixels = []
for row in range(6):
    pixelRow = ""
    for col in range(1, 41):
        cycle = row * 40 + col
        sprite = range(valueAt[cycle], valueAt[cycle] + 3)
        # is the first cycle affected?
        if col in sprite:
            pixelRow += "#"
        else:
            pixelRow += "."
    pixels.append(pixelRow)

print(valueAt[:15])
for row in pixels:
    print(row)

