from pprint import pprint
from copy import deepcopy
    


#openList: Noder til naboene som er besokt.
#closedList: Noder som er besokt!



def loadFile(input):
    f = open(input, 'r')
    x = f.readlines()
    f.close()

    myArray = []
    for element in x:
        element = element.replace('\n', '')
        element = [element]
        element = list(element[0])
        myArray.append(element)
    return myArray

def findA(array):
    return ([(i, arr.index('A'))
     for i, arr in enumerate(array)
     if 'A' in arr])

def findB(array):
    return ([(i, arr.index('B'))
     for i, arr in enumerate(array)
    if 'B' in arr])

def findCost(char):
    return {
        '.': 1,
        'A': 1,
        'B': 1,
        'r': 1,
        'g': 5,
        'f': 10,
        'm': 50,
        'w': 100
    }.get(char, -1)

class Node():
    def __init__(self, parent=None, position=None, cost = 0):


        # Variables that are contained in each node:
        self.parent = parent
        self.position = position
        self.cost = cost
        self.children = []

        self.g = 0  # Avstanden fra start til den aktuelle noden
        self.h = 0  # heuristic (Avstanden til goalnoden)
        self.f = 0  # g+h

        ##Metode som retur true om posisjonen er lik for to objekter.

    def __eq__(self, other):
        return self.position == other.position


def astar(grid, start, end):
    grid_copy = deepcopy(grid)

    # Setting start and end node:
    startNode = Node(None, start, 0)  # Giving it the parent = Null and start (row,col)
    startNode.g = 0

    end_cost = findCost(grid[end[0]][end[1]])
    if end_cost == -1:
        print('Goal node is illegal')
        return -1

    endNode = Node(None, end, end_cost)
    endNode.g = endNode.h = endNode.f = 0

    startNode.h = ((startNode.position[0] - endNode.position[0]) ** 2) + ((startNode.position[1] - endNode.position[1]) ** 2)
    startNode.f = startNode.g + startNode.h

    # The lists:
    openList = []
    closedList = []

    # Adding the start and end-node to the arrays:
    openList.append(startNode)

    # Main loop
    while len(openList)>0:

        # get the current node (The first element, since we are appending from the front!)
        currentNode = openList[0]
        currentIndex = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index
        # Pop current off list and add to closed list
        openList.pop(currentIndex)
        closedList.append(currentNode)

        grid_copy[currentNode.position[0]][currentNode.position[1]] = '~'


        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                grid_copy[current.position[0]][current.position[1]] = 'U'
                current = current.parent
            return path[::-1]

        # For printing visited nodes
        #for line in maze_copy:
        #    for char in line:
        #        print(char, end="", flush=True)
        #    print('\n')
        #print('\n')


        # find children of current node:
        # Children positions:
        children = []

        checkList = []
        cPos = currentNode.position
        childDownPos = (cPos[0] + 1, cPos[1])
        checkList.append(childDownPos)

        childUpPos = ((cPos[0]) - 1, cPos[1])
        checkList.append(childUpPos)

        childRghtPos = (cPos[0], cPos[1] + 1)
        checkList.append(childRghtPos)

        childLftPos = (cPos[0], cPos[1] - 1)
        checkList.append(childLftPos)

        # Check the new positions (Not outside grid and in blocked:
        #print((len(grid)) - 1 )
        #print("Dette over er len(grid)-1")
        #print((len(grid[0]) - 1))
        for x in checkList:
            terrain_cost = -1
            if x[0] > len(grid) - 1 or x[0] < 0 or x[1] > len(
                    grid[len(grid) - 1]) - 1 or x[1] < 0:
                continue

            # check if there is a blocking there!
            if grid[x[0]][x[1]] == '#':
                continue
            terrain_cost = findCost(grid[x[0]][x[1]])
            if terrain_cost == -1:
                continue
            # Setting parent and position of child:
            newNode = Node(currentNode, x,terrain_cost)
            # Adding childnode to children of parent-array.
            children.append(newNode)

            # Loop through children and check if child has already been traversed or add to open list
        for child in children:
            tempG = currentNode.g + child.cost
            tempH = abs(child.position[0] - endNode.position[0]) + abs(child.position[1] - endNode.position[1])
            tempF = tempG + tempH

            if child in openList:
                if tempG < child.g:
                    child.g = tempG
                    child.parent = currentNode
            elif child in closedList:
                continue
                # propagateImprovements(child)
            else:
                # Calculate g, h and f value
                child.g = tempG
               # Using Euclidean distance
                child.h = tempH
                # Update f value
                child.f = tempF

                child.parent = currentNode
                openList.append(child)
    return -1


def main():
    # READING BOARD (.txt-file) *****
    #board = input()
    maze2 = loadFile('board-2-4.txt')
    #maze2 = loadFile(board)
    start = (findA(maze2))[0]
    end = (findB(maze2))[0]
    path = astar(maze2, start, end)
    for tuple in path:
        if tuple[0]==start[0] and tuple[1]==start[1]:
            maze2[tuple[0]][tuple[1]]='A'
        elif tuple[0]==end[0] and tuple[1]==end[1]:
            maze2[tuple[0]][tuple[1]]='B'
        else:
            maze2[tuple[0]][tuple[1]] = 'X'
    for row in maze2:
        for char in row:
            print (char, '  ', end="", flush=True)
        print('\n')

if __name__ == '__main__':
    main()