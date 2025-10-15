def cacti_number(plot):
    """
    Given a 2-D list of 0/1 where 1 = existing cactus and 0 = empty,
    return the maximum number of additional cacti that can be planted
    so that no two cacti are adjacent horizontally or vertically.
    """
    if not plot:
        return 0

    rows = len(plot)
    cols = len(plot[0])

    grid = [row[:] for row in plot]

    def has_adjacent_one(r, c):
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                return True
        return False

    planted = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and not has_adjacent_one(r, c):
                grid[r][c] = 1   # plant here
                planted += 1

    return planted
