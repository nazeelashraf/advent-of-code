from collections import deque

count = 0

grid = []
misunderstood = False

with open("input.txt", "r") as file:
    line = file.readline().strip()

    while line:
        grid.append(list(line))
        line = file.readline().strip()

nextLetterMap = {"X": "M", "M": "A", "A": "S", "S": ""}

print(grid)
ROWS = len(grid)
COLS = len(grid[0])

initialDirections = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]


def bfs(r, c):
    if grid[r][c] != "X":
        return 0
    queue = deque()
    xmasCount = 0

    queue.append((r, c, initialDirections))

    while queue:
        row, col, directions = queue.popleft()

        if grid[row][col] == "S":
            xmasCount += 1
            continue

        for dr, dc in directions:
            newR, newC = row + dr, col + dc

            if (
                newR >= 0
                and newC >= 0
                and newR < ROWS
                and newC < COLS
                and grid[newR][newC] in nextLetterMap
            ):
                newLetter = grid[newR][newC]
                if newLetter == nextLetterMap[grid[row][col]]:
                    queue.append((newR, newC, [[dr, dc]]))

    return xmasCount


allCombinations = [
    ([-1, -1], [0, 0], [1, 1]),
    ([-1, 1], [0, 0], [1, -1]),
    ([1, -1], [0, 0], [-1, 1]),
    ([1, 1], [0, 0], [-1, -1]),
]


def isXHyphenMAS(r, c):
    for dr, dc in initialDirections:
        newR, newC = r + dr, c + dc
        if not ((0 <= newR < ROWS) and (0 <= newC < COLS)):
            return 0
    allStrings = []
    for combination in allCombinations:
        string = ""
        for dr, dc in combination:
            string += grid[r + dr][c + dc]
        allStrings.append(string)

    if allStrings.count("MAS") == 2 and allStrings.count("SAM") == 2:
        return 1
    return 0


for r in range(len(grid)):
    for c in range(len(grid[0])):
        if misunderstood:
            if grid[r][c] == "X":
                count += bfs(r, c)
        else:
            if grid[r][c] == "A":
                count += isXHyphenMAS(r, c)

print(f"Number of XMAS: {count}")
