import sys


grid = []
currentPoint = (0, 0)

filePath = "input.txt"

args = sys.argv[1:]
if args:
    filePath = args[-1]

with open(filePath, "r") as file:
    line = file.readline().strip()
    i = 0
    while line:
        if "^" in line:
            currentPoint = (i, line.index("^"))
        grid.append(list(line))
        i += 1
        line = file.readline().strip()

ROWS, COLS = len(grid), len(grid[0])
direction = (-1, 0)

directionMap = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


def isValidPosition(r, c):
    return r >= 0 and r < ROWS and c >= 0 and c < COLS


def isObstacle(r, c):
    return grid[r][c] == "#"


def gridPrinter():
    for row in grid:
        print(row)


def setObstacles(obstacles):
    for r, c in obstacles:
        grid[r][c] = "O"


def isCyclePath(r, c, direction):
    visited = set()
    while isValidPosition(r, c):
        dr, dc = direction
        while isValidPosition(r + dr, c + dc) and isObstacle(r + dr, c + dc):
            if (r, c, direction) in visited:
                return True
            visited.add((r, c, direction))
            direction = directionMap[direction]
            dr, dc = direction
        if (r, c, direction) in visited:
            return True
        visited.add((r, c, direction))

        dr, dc = direction
        r, c = r + dr, c + dc

    return False


count = 0
obstaclePositions = set()
r, c = currentPoint
while True:
    if grid[r][c] != "X":
        grid[r][c] = "X"
        count += 1
    dr, dc = direction
    nextR, nextC = r + dr, c + dc

    if not isValidPosition(nextR, nextC):
        break

    while isObstacle(nextR, nextC):
        direction = directionMap[direction]
        dr, dc = direction
        nextR, nextC = r + dr, c + dc

    if grid[nextR][nextC] != "X":
        lastValue = grid[nextR][nextC]
        grid[nextR][nextC] = "#"

        if isCyclePath(r, c, direction):
            obstaclePositions.add((nextR, nextC))
        grid[nextR][nextC] = lastValue
    r, c = nextR, nextC

if currentPoint in obstaclePositions:
    obstaclePositions.remove(currentPoint)
# setObstacles(obstaclePositions)
# gridPrinter()
print(count, len(obstaclePositions))
