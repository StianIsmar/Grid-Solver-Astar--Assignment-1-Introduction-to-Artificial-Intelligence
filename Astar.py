from pprint import pprint
#openList: Noder til naboene som er besokt.
#closedList: Noder som er besokt!
class Node():
    def __init__(self, parent=None, position=None):
        
        # Variables that are contained in each node:
        self.parent = parent
        self.position = position
        self.g = 0  # Avstanden fra start til den aktuelle noden
        self.h = 0  # heuristic (Avstanden til goalnoden)
        self.f = 0  # g+h

        ##Metode som retur true om posisjonen er lik for to objekter.

    def __eq__(self, other):
        self.position == other.position


def astar(grid, start, end):
    # Setting start and end node:
    startNode = Node(None, start)  # Giving it the parent = Null and start (row,col)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.h = endNode.f = endNode.g = 0

    pprint(vars(startNode))

    # The lists:
    openList = []
    closedList = []

    # Adding the start and end-node to the arrays:
    openList.append(startNode)
    print(openList)

    # Main loop
    while len(openList) > 0:

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

        if currentNode == endNode:
            # Har funnet endenoden. Returner pathen fra start til slutt!
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        else:
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
            for x in checkList:
                if (x[0] < 0 or x[1] < 0 or x[0] > (len(grid)) - 1) or x[1] < (len(grid[0]) - 1):
                    continue
                # check if there is a blocking there!
                if grid[x[0]][x[1]] == '#':
                    continue
                else:
                    newNode = Node(currentNode, x)
                    children.append(newNode)

            # looping through the added children:
        for child in children:

            # Child is on the closed list
            for closedChild in closedList:
              if closedChild == child:
                    continue
            # if not on the closedList (It is not expanded)
            # find the values for that particular child:
            child.g = currentNode.g + 1
            child.h = (child.position[0] ** 2 - currentNode.position[0] ** 2) + (
                child.position[1] ** 2 - currentNode.position[1] ** 2)
            child.f = child.g + child.f

            #Child already in openList?
            for openNode in openList:
                if (child == openNode and child.g > openNode.g):
                    # Da er den aktuelle barnenoden allerede i openNode, altså er den "oppdaget" før (men
                    # ikke besøkt). Sjekker også om g-verdien (avstanden fra start (,) til barnet er større enn
                    # avstanden fra start til
                    continue




            children.append((currentNode.position))
            # set their g, h and f values!


def main():
    # READING BOARD (.txt-file) *****
    '''list_of_lists = []
    with open("/Users/stianismar/Dropbox/Trondheim/H18/Intro til kunstig intelligens/Innlevering 2/board11.txt") as f:
    for line in f:
    inner_list = [elt.strip() for elt in line.split(',')]
    # in alternative, if you need to use the file content as numbers
    # inner_list = [int(elt.strip()) for elt in line.split(',')]
    list_of_lists.append(inner_list)

    grid = list_of_lists

    THE START AND END
    start = (3,13)
    end = (3,17 )
'''
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # path = astar(maze, (3,13),(3,17))
    start = (0, 0)
    end = (7, 6)
    path = astar(maze, start,end)


if __name__ == '__main__':
    main()