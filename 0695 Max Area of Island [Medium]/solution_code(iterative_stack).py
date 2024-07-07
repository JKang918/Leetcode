def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    m = len(grid)    #row size
    n = len(grid[0]) #col size
    
    def island(row, col) -> bool:
        return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
    
    def dfs(row, col) -> int:
        area = 1
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            for dx, dy in direction:
                if island(r + dx, c + dy) and (r + dx, c + dy) not in seen:
                    seen.add((r + dx, c + dy))
                    area += 1
                    stack.append((r + dx, c + dy))
        return area
    
    maxarea = 0
    seen = set()

    for row in range(m):
        for col in range(n):
            if island(row, col) and (row, col) not in seen:
                seen.add((row, col))
                maxarea = max(maxarea, dfs(row, col))
    
    return maxarea