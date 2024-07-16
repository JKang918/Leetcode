from typing import List
from collections import deque

def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:

    #nearest exit -> shortest path -> BFS

    m = len(maze)
    n = len(maze[0])

    #each step: UP, DOWN, LEFT, RIGHT
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    #exit is border cells #entrance does not count as an exit
    def isExit(r, c):
        return (r == m - 1 or r == 0 or c == n - 1 or c == 0) and ([r, c] != entrance)
    
    #Valid cell to move on
    def isValidpath(r, c):
        return 0 <= r < m and 0 <= c < n and maze[r][c] == "."

    #starting coordinate and current step = 0
    queue = deque([(entrance[0], entrance[1], 0)])
    seen = {(entrance[0], entrance[1])}

    while queue:
        curr_len = len(queue)

        for _ in range(curr_len):

            r, c, steps = queue.popleft()

            #if exit reached
            if isExit(r, c):
                return steps
            
            for dx, dy in directions:
                if (r + dx, c + dy) not in seen and isValidpath(r + dx, c + dy):
                    seen.add((r + dx, c + dy))
                    queue.append((r + dx, c + dy, steps + 1))
            
    return -1