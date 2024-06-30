def numIslands(grid: list[list[str]]) -> int:
    
    m = len(grid)    #num of rows
    n = len(grid[0]) #num of cols
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

    def isValid(row, col) -> bool:
        return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"  

    def dfs(row: int, col: int) -> None:
        #search neighbors
        for dx, dy in directions:
            if isValid(row + dx, col + dy) and (row + dx, col + dy) not in seen:
                seen.add((row + dx, col + dy))
                dfs(row + dx, col + dy)
        return

    seen = set()
    count = 0
    for r in range(m):
        for c in range(n):
            if isValid(r, c) and (r, c) not in seen:
                seen.add((r, c))
                dfs(r, c)
                count += 1

    return count