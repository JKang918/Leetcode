def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    m = len(grid)    #row size
    n = len(grid[0]) #col size
    
    def island(row, col) -> bool:
        return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
    
    def dfs(row, col) -> int:
        area = 1
        for dx, dy in direction:
            if island(row + dx, col + dy) and (row + dx, col + dy) not in seen:
                seen.add((row + dx, col + dy))
                area += dfs(row + dx, col + dy)
        return area #return 1 if base case

    
    
    maxarea = 0
    seen = set()

    for row in range(m):
        for col in range(n):
            if island(row, col) and (row, col) not in seen:
                seen.add((row, col))
                maxarea = max(maxarea, dfs(row, col))
    
    return maxarea