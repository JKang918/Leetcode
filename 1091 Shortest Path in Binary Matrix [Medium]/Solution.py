from collections import deque
from typing import List
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    #shortest path -> BFS
    
    #row bound
    m = len(grid)
    #col bound
    n = len(grid[0])
    
    #possible search directions
    directions = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1))
    
    #to avoid duplicate path
    seen = {(0, 0)}
    
    #check whether a certain grid is valid path
    def IsValid(r, c):
        return 0 <= r < m and 0 <= c < n and grid[r][c] == 0 

    #BFS
    #row, col, path
    queue = deque([(0, 0, 1)])

    #starting point check
    if grid[0][0] == 1: return -1

    while queue:
        curr_len = len(queue)

        for _ in range(curr_len):
            r, c, path = queue.popleft()

            ##
            if r == m - 1 and c == n - 1:
                return path
            ##

            for dx, dy in directions:
                if (r + dx, c + dy) not in seen and IsValid(r + dx, c + dy):
                    seen.add((r + dx, c + dy))
                    queue.append((r + dx, c + dy, path + 1))
    
    return -1


    