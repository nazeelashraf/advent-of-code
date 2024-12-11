map = []
distinct = True
with open("input.txt", "r") as file:
    line = file.readline().strip()

    while line:
        map.append([int(val) for val in list(line)])
        line = file.readline().strip()

ROWS, COLS = len(map), len(map[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(r, c, visited):
    if map[r][c] == 9 and (r, c) not in visited:
        if not distinct:
            visited.add((r, c))
        return 1

    score = 0
    for dr, dc in directions:
        newR, newC = r + dr, c + dc
        if (
            (0 <= newR < ROWS)
            and (0 <= newC < COLS)
            and map[newR][newC] == map[r][c] + 1
        ):
            score += dfs(newR, newC, visited)

    return score


totalCount = 0
for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == 0:
            totalCount += dfs(r, c, set())

print(totalCount)
