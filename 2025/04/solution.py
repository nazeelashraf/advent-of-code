grid = []
positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
R, C = 0, 0


def print_grid():
    for row in grid:
        print("".join(row))


def is_paper_roll(x: int, y: int):
    if 0 <= x < R and 0 <= y < C:
        return grid[x][y] == "@"
    return False


def can_access(x: int, y: int):
    count = 0
    for dx, dy in positions:
        _x, _y = x + dx, y + dy
        if is_paper_roll(_x, _y):
            count += 1

    if count < 4:
        grid[x][y] = "x"
        return True

    return False


with open("input.txt") as file:
    line = file.readline().strip()

    while line:
        grid.append(list(line))
        line = file.readline().strip()

    R, C = len(grid), len(grid[0])


def get_total_count():
    total_count = 0
    for r in range(0, R):
        for c in range(0, C):
            if grid[r][c] == "@" and can_access(r, c):
                total_count += 1

    return total_count


current_total_count = get_total_count()
total_count = current_total_count

while current_total_count != 0:
    current_total_count = get_total_count()
    total_count += current_total_count

print_grid()
print(f"total count: {total_count}")
