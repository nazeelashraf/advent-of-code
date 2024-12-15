import re

pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
robots = []
ROWS, COLS = 103, 101
with open("input.txt", "r") as file:
    line = file.readline().strip()

    while line:
        matches = re.findall(pattern, line)
        robots.append(
            [
                int(matches[0][0]),
                int(matches[0][1]),
                int(matches[0][2]),
                int(matches[0][3]),
            ]
        )
        line = file.readline().strip()

quadrantLimits = {
    1: (0, 0, COLS // 2, ROWS // 2),
    2: (0, ROWS // 2 + 1, COLS // 2, ROWS - 1),
    3: (COLS // 2 + 1, 0, COLS - 1, ROWS // 2),
    4: (COLS // 2, ROWS // 2, COLS - 1, ROWS - 1),
}


def isInQuadrant(x, y):
    return x != COLS // 2 and y != ROWS // 2


def getQuadrant(x, y):
    for quadrant, bounds in quadrantLimits.items():
        xMin, yMin, xMax, yMax = bounds
        if (xMin <= x <= xMax) and (yMin <= y <= yMax):
            return quadrant


def printGrid(robots):
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for x, y in robots:
        grid[y][x] += 1

    print("-----------")
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                grid[y][x] = "."
    for row in grid:
        print("".join([str(val) for val in row]))
    print("-----------")


t = 0
quadrantCount = {1: 0, 2: 0, 3: 0, 4: 0, None: 0}
newRobots = set()


points = [
    (ROWS // 2, 0),
    (ROWS // 2 - 1, 1),
    (ROWS // 2 + 1, 1),
    (ROWS // 2 - 2, 2),
    (ROWS // 2 + 2, 2),
]


def heuristic1():
    global newRobots

    hasPoint = True
    for point in points:
        hasPoint = hasPoint and point in newRobots

    return hasPoint


def run():
    global newRobots
    global quadrantCount
    global t
    for robot in robots:
        x, y, dx, dy = robot

        newX, newY = (x + t * dx) % COLS, (y + t * dy) % ROWS

        if isInQuadrant(newX, newY):
            quadrantCount[getQuadrant(newX, newY)] += 1

        newRobots.add((newX, newY))


entry = input("Solution 1 or 2? (q to quit)")
alternate = False
if entry == "1":
    t = 100
else:
    t = 39
t1, t2 = 60, 41
solutionPicked = entry
while entry != "q":
    newRobots = set()
    quadrantCount = {1: 0, 2: 0, 3: 0, 4: 0, None: 0}

    run()
    if solutionPicked == "1":
        break
    printGrid(newRobots)
    entry = input(f"T = {t}. Press enter until T=7412 (q to quit)")
    if t == 7412:
        break

    if alternate:
        t += t2
        t2 -= 2
    else:
        t += t1
        t1 += 2
    alternate = not alternate

total = 1

for key, value in quadrantCount.items():
    if key:
        total *= value
print(quadrantCount)
print(f"Safety factor: {total}")
