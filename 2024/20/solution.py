from math import ceil, floor, sqrt
import heapq
import sys
from collections import defaultdict, deque

grid = []
startingPoint = (0, 0)
with open("input.txt", "r") as file:
    line = file.readline().strip()

    while line:
        if "S" in line:
            startingPoint = (len(grid), line.index("S"))
        grid.append(list(line))
        line = file.readline().strip()

print(len(grid), len(grid[0]))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

ROWS, COLS = len(grid), len(grid[0])


def isValidPosition(r, c):
    return (0 <= r < ROWS) and (0 <= c < COLS) and grid[r][c] != "#"


sys.setrecursionlimit(10000)


def dfs(r, c, visited, depth):
    if grid[r][c] == "E":
        visited[(r, c)] = depth
        return visited
    if not isValidPosition(r, c) or (r, c) in visited:
        return None

    visited[(r, c)] = depth

    for dr, dc in directions:
        result = dfs(r + dr, c + dc, visited, depth + 1)
        if result:
            return result

    del visited[(r, c)]


def euclideanDistance(point1, point2):
    r1, c1 = point1
    r2, c2 = point2

    return sqrt(abs((r1 - r2) ** 2 + (c1 - c2) ** 2))


def getClosePoints(points):
    minHeap = []
    totalPicoseconds = len(points)

    queue = deque()

    for key, value in points.items():
        queue.append((key, value))
    print(queue)

    while queue:
        point1, distanceFromStart1 = queue.popleft()

        for point2, distanceFromStart2 in queue:
            distance = euclideanDistance(point1, point2)
            if distance <= 3:
                newDistance = (
                    distanceFromStart1
                    + (totalPicoseconds - distanceFromStart2)
                    + ceil(distance)
                )
                if newDistance < totalPicoseconds - 1:
                    heapq.heappush(minHeap, (newDistance, point1, point2))

    return minHeap


r, c = startingPoint
pathPoints = dfs(r, c, {}, 0)
print(pathPoints, len(pathPoints))

minHeap = getClosePoints(pathPoints)
print(minHeap, len(minHeap))

countFreq = defaultdict(int)

while minHeap:
    distance, point1, point2 = heapq.heappop(minHeap)

    countFreq[distance] += 1

print(countFreq)
