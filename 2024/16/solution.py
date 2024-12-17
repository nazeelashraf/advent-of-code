import heapq

grid = []
startingPoint = (0, 0)
with open("input.txt", "r") as file:
    line = file.readline().strip()

    while line:
        print(line)
        grid.append(list(line))
        if "S" in line:
            startingPoint = (len(grid) - 1, line.find("S"))
        line = file.readline().strip()
startingDirection = (0, 1)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
print(len(grid), len(grid[0]))


def isValidPosition(r, c):
    return grid[r][c] != "#"


def dijkstra(r, c, startDir):
    shortest = {}
    shortestE = float("inf")

    minHeap = [(0, r, c, startDir)]

    while minHeap:
        weight, r, c, direction = heapq.heappop(minHeap)
        if (r, c, direction) in shortest:
            continue
        shortest[(r, c, direction)] = weight
        if grid[r][c] == "E":
            shortestE = min(shortestE, weight)

        for dir in directions:
            dr, dc = dir
            _r, _c = r + dr, c + dc
            if not isValidPosition(_r, _c):
                continue
            points = 1
            if direction != dir:
                points = 1001
            if dir == (-direction[0], -direction[1]):
                points = 2001
            newHeapValue = (_r, _c, dir)
            if newHeapValue not in shortest:
                heapq.heappush(minHeap, (weight + points, _r, _c, dir))

    return shortestE


minScore = dijkstra(startingPoint[0], startingPoint[1], startingDirection)
print(startingPoint, minScore)
