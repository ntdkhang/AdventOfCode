file = open("./inputs/input11.txt", "r")

lineIndex = 0
monkeys = []
    
class Monkey:
    leastCommonMultiple = 1
    def __init__(self):
        self.starting = []
        self.operation = ""
        self.testDivisible = 0
        self.monkeyWhenTrue = -1
        self.monkeyWhenFalse = -1
        self.numInspections = 0

    def operate(self):
        starting = self.starting
        self.starting = []
        for item in starting:
            # perform operation         
            other = self.operation.split()[-1]
            if other == "old":
                num = item 
            else:
                num = int(other)
            
            if self.operation.split()[-2] == "*":
                num = num * item
            else: # plus +
                num = num + item

            # increase count inspection 
            self.numInspections += 1

            # divide value by 3
            num = num % self.leastCommonMultiple

            # test divisible 
            # throw to other monkey 
            if num % self.testDivisible == 0:
                monkeys[self.monkeyWhenTrue].starting.append(num)
            else:
                monkeys[self.monkeyWhenFalse].starting.append(num)


for line in file:
    if lineIndex == 0:
        newMonkey = Monkey()
        monkeys.append(newMonkey)
    if lineIndex == 1:
        monkeys[-1].starting = [int(x) for x in line[18:-1].split(", ")]
    if lineIndex == 2:
        monkeys[-1].operation = line[14:-1]
    if lineIndex == 3:
        monkeys[-1].testDivisible = int(line.split()[-1])
        Monkey.leastCommonMultiple *= monkeys[-1].testDivisible
    if lineIndex == 4:
        monkeys[-1].monkeyWhenTrue = int(line.split()[-1])
    if lineIndex == 5:
        monkeys[-1].monkeyWhenFalse = int(line.split()[-1])

    lineIndex = (lineIndex + 1) % 7

# uncomment for part 1
"""
for i in range(20):
    for monkey in monkeys:
        monkey.operate()

inspectCount = [x.numInspections for x in monkeys]
sortedInspection = sorted(inspectCount, reverse=True)
print(sortedInspection)
print(sortedInspection[0] * sortedInspection[1])
"""

# Part 2:
print("PART 2")
for i in range(10000):
    for monkey in monkeys:
        monkey.operate()

inspectCount = [x.numInspections for x in monkeys]
sortedInspection = sorted(inspectCount, reverse=True)
print(sortedInspection)
print(sortedInspection[0] * sortedInspection[1])





