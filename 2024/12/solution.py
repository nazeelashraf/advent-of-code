from collections import deque

grid = []

visited = set()

isDiscount = False

with open("input.txt", "r") as file:
    line = file.readline().strip()

    while line:
        grid.append(list(line))
        line = file.readline().strip()

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ROWS, COLS = len(grid), len(grid[0])


def isValidPosition(r, c, val):
    return (0 <= r < ROWS) and (0 <= c < ROWS) and grid[r][c] == val


def getGoodNeighbours(r, c):
    if (r, c) in visited:
        return []
    neighbours = []

    for dr, dc in directions:
        if isValidPosition(r + dr, c + dc, grid[r][c]):
            neighbours.append((r + dr, c + dc))

    return neighbours


def findEdges(nodes):
    verticalEdgeCount = 0
    horizontalEdgeCount = 0

    horizontal = sorted(nodes, key=lambda s: (s[0], s[1]))
    vertical = sorted(nodes, key=lambda s: (s[1], s[0]))

    isHorizontal = False
    isVertical = False
    for i in range(1, len(horizontal)):
        newIsHorizontal = (
            horizontal[i][0] == horizontal[i - 1][0]
            and horizontal[i][1] == horizontal[i - 1][1] + 1
        )
        newIsVertical = (
            vertical[i][1] == vertical[i - 1][1]
            and vertical[i][0] == vertical[i - 1][0] + 1
        )
        if newIsHorizontal and not isHorizontal:
            horizontalEdgeCount += 1
        if newIsVertical and not isVertical:
            verticalEdgeCount += 1

        isHorizontal, isVertical = newIsHorizontal, newIsVertical

    print("----")
    print(horizontal, horizontalEdgeCount * 2)
    print(vertical, verticalEdgeCount * 2)
    print("----")

    return horizontalEdgeCount + verticalEdgeCount


def bfs(row, col):
    queue = deque()
    area, perimeter = 0, 0
    queue.append((row, col))

    allNeighbours = set()
    allNeighbours.add((row, col))

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) in visited:
                continue
            goodNeighbours = getGoodNeighbours(r, c)
            area += 1
            perimeter += len(directions) - len(goodNeighbours)
            visited.add((r, c))

            for neighbour in goodNeighbours:
                queue.append(neighbour)
                allNeighbours.add(neighbour)

    if isDiscount:
        perimeter = findEdges(list(allNeighbours))
    return area, perimeter


totalCost = 0
for r in range(ROWS):
    for c in range(COLS):
        if (r, c) not in visited:
            area, perimeter = bfs(r, c)
            totalCost += area * perimeter

print(totalCost)
