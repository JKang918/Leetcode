## 1926. Nearest Exit from Entrance in Maze
 
>Description: [1926. Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/)\
Check out the link for description

Constraints:

- `maze.length == m`
- `maze[i].length == n`
- `1 <= m, n <= 100`
- `maze[i][j] is either '.' or '+'.`
- `entrance.length == 2`
- `0 <= entrancerow < m`
- `0 <= entrancecol < n`
- `entrance will always be an empty cell.`

### Solution

```python
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
```

### Breakdown of Solution:

When a graph problem requires finding the shortest path, using BFS is more useful than DFS. BFS explores the graph level by level, making it easy to stop when the goal is reached and return the number of steps taken.

Below are a few takeaways from this solution:

#### additional requirements (varys by each problem)

```python
    #exit is border cells #entrance does not count as an exit
    def isExit(r, c):
        return (r == m - 1 or r == 0 or c == n - 1 or c == 0) and ([r, c] != entrance)
```
- this problem specifically states that entrance (starting grid) should not be the ending point. Hence, `[r, c] != entrance` is added.

#### store steps (distance, level, etc) information in the queue as well

```python
#starting coordinate and current step = 0
    queue = deque([(entrance[0], entrance[1], 0)])
    seen = {(entrance[0], entrance[1])}

...

            for dx, dy in directions:
                if (r + dx, c + dy) not in seen and isValidpath(r + dx, c + dy):
                    seen.add((r + dx, c + dy))
                    queue.append((r + dx, c + dy, steps + 1))
```

- not only the coordinate of the grid of interest, store how many `steps` taken as well. This is to track the distance (levels) from the original starting point.


All the rest are typical BFS solution for when input is matrix with each grid representing each node.

### Complexity Analysis:

Time Complexity: *O(m * n)*

- traverse the input

Space Complexity: *O(m * n)* or *O(1)*

- O(m * n) if using copied object. O(1) if sticking to input and modify the input.