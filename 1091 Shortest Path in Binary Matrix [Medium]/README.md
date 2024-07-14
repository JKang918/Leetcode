## 1091. Shortest Path in Binary Matrix

>Description: [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)\
Check out the link above for description.

Constraints:

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j] is 0 or 1`


### Solution: 

```python
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
```
### Breakdown of Solution:

It is known that efficiently constructed breadth first search (BFS) is almost identical to depth first search (DFS) in terms of performance. As DFS is easier to code, oftentimes DFS is preferred over BFS.

However, there are some instances where BFS shines over DFS, one of which is 'finding the shortest path' type of problems.

That is because as in the case of binary tree, in graph problems, instead of getting further away from the original starting point, BFS visits nodes in accordance to their distance from the starting point.

In the above code, that distance information is separtely stored in the `queue` along with grid information. Everytime node one distance greater is searched, `path + 1` is added to the deque. 

### Complexity Analysis:

Time Complexity: *O(m*n)*

- linearly correlated with the number of cells

Space Complexity: *O(m*n)*

- max size is the deque
