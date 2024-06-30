def numIslands(self, grid: list[list[str]]) -> int:
    
    m = len(grid)    #num of rows
    n = len(grid[0]) #num of cols
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

    def isValid(row, col) -> bool:
        return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"  

    def dfs(row: int, col: int) -> None:
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            for dx, dy in directions:
                if isValid(r + dx, c + dy) and (r + dx, c + dy) not in seen:
                    seen.add((r + dx, c + dy))
                    stack.append((r + dx, c + dy))
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