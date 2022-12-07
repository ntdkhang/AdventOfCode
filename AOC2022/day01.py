file = open("./inputs/input01.txt", "r")

elfsCarry = [0]
for line in file:
    if line != "\n":
        elfsCarry[-1] += int(line[:-1])
    else:
        elfsCarry.append(0)

# 1st task
print(max(elfsCarry))

#2nd task
sortedElfs = sorted(elfsCarry, reverse=True)

print(sum(sortedElfs[:3]))
