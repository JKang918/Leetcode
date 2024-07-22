from typing import List
from collections import deque

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:

    m = len(mat)
    n = len(mat[0])
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    def isValid(x, y):
        return 0 <= x < m and 0 <= y < n

    #seen has all of zero cells
    seen = set()
    queue = deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] not in seen and mat[i][j] == 0:
                seen.add((i, j))
                queue.append((i, j, 0))
    
    while queue:

        r, c, steps = queue.popleft()
        
        for dx, dy in directions:
            new_r = r + dx
            new_c = c + dy 
            if isValid(new_r, new_c) and (new_r, new_c) not in seen:
                seen.add((new_r, new_c))
                queue.append((new_r, new_c, steps + 1))
                mat[new_r][new_c] = steps + 1
    
    return mat