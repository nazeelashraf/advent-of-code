from collections import deque

grid = []

visited = set()

isDiscount = True

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


cornerPositions = [
    ((1, 1), (1, 0), (0, 1)),
    ((-1, -1), (-1, 0), (0, -1)),
    ((1, -1), (0, -1), (1, 0)),
    ((-1, 1), (-1, 0), (0, 1)),
]


def getCorners(r, c):
    corners = 0
    val = grid[r][c]
    for (dr, dc), (dra, dca), (drb, dcb) in cornerPositions:
        if (
            isValidPosition(r + dr, c + dc, val)
            and isValidPosition(r + dra, c + dca, val)
            == isValidPosition(r + drb, c + dcb, val)
            == False
        ):
            corners += 1
        elif not isValidPosition(r + dr, c + dc, val) and isValidPosition(
            r + dra, c + dca, val
        ) == isValidPosition(r + drb, c + dcb, val):
            corners += 1

    return corners


def bfs(row, col):
    queue = deque()
    area, perimeter = 0, 0
    queue.append((row, col))

    corners = 0

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) in visited:
                continue
            goodNeighbours = getGoodNeighbours(r, c)
            area += 1
            perimeter += len(directions) - len(goodNeighbours)
            visited.add((r, c))
            corners += getCorners(r, c)

            for neighbour in goodNeighbours:
                queue.append(neighbour)
                # allNeighbours.add(neighbour)

    if isDiscount:
        perimeter = corners
    return area, perimeter


totalCost = 0
for r in range(ROWS):
    for c in range(COLS):
        if (r, c) not in visited:
            area, perimeter = bfs(r, c)
            totalCost += area * perimeter
print(totalCost)
