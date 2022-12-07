file = open("./inputs/input07.txt", "r")

class Item:
    def __init__(self, name, size = None, parent = None):
        self.name = name 
        self.size = size
        self.parent = parent

    def getSize(self):
        if self.size:
            return self.size 
        else:
            return 0

class File(Item):
    def __init__(self, name, size = None, parent = None):
        Item.__init__(self, name, size, parent)
     

class Directory(Item):
    def __init__(self, name, size = None, parent = None):
        Item.__init__(self, name, size, parent)
        self.subDir = []

    def calculateSize(self):
        # update size of directory here
        return

root = Directory(name="/")
currentDir = root
sumSize = 0

def changeDir(newDirectoryName):
    global currentDir
    newDir = Directory(name=newDirectoryName, parent=currentDir)
    currentDir.subDir.append(newDir)
    currentDir = newDir 

def sizeOf(item) -> int: 
    global sumSize
    if isinstance(item, File):
        return item.getSize()
    else: # directory
        totalSize = 0
        for subItem in item.subDir:
            totalSize += sizeOf(subItem)
        item.size = totalSize
        if totalSize < 100000:
            sumSize += totalSize
        return totalSize

for line in file:
    if line[0] == "$": # commands
        if line[2:4] == "cd":
            newDirName = line[5:-1]
            if newDirName == "..": 
                currentDir = currentDir.parent
            else:
                changeDir(newDirName)
        else: # ls command, basically can be ignored
            continue
    else: # listing files and directories
        if line[0].isnumeric(): # file. "1234 h"
            newFile = File(name=line.split()[1], size=int(line.split()[0]), parent=currentDir)
            # print(newFile.name)
            currentDir.subDir.append(newFile)

def sizeToDelete(directory):
    global minimumSize
    for subItem in directory.subDir:
        if isinstance(subItem, Directory) and subItem.getSize() > sizeRequired:
             minimumSize = min(minimumSize, subItem.getSize())
             sizeToDelete(subItem)

rootSize = sizeOf(root)
sizeRequired = 30000000 - (70000000 - rootSize)
minimumSize = rootSize
sizeToDelete(root)

print(sumSize)
print(rootSize)
print(minimumSize)



