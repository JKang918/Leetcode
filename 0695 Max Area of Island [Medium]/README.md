## 695. Max Area of Island

>Description: [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)\
Check out the link above

Constraints:

- `m == grid.length`
- `n == grid[i].length`
- <code>1 <= m, n <= 50</code> 
- `grid[i][j]` is `'0'` or `'1'`.


### Solution 1: DFS with recursive function 

```python
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
```
### Breakdown of Solution:

**Depth First Search (Graph)**

Input matrix: each element in a matrix represents each vertex in a graph

Meaning of Islands: connected in the four dirctions(up, down, left, right) -> connected components

Meaning of Area of Islands: Number of (i, j) where `grid[i][j] == 1`.

This problem is asking you to get the number of cells in a connected components in a given graph, which is suited for DFS approach.

The only thing to take note of here is how DFS is implemented.

1. `isLand()` function

    - It is to simplify the process of finding connected vertices to a given vertex.
    - If a neighboring vertex is `"1"` then this is connected.

2. `dfs()` function

    - if a neighboring vertex is valid ( = connected), then call the recursive function, `dfs()`
    - in a base case, return 1.
    - `area += dfs(row + dx, col + dy)` and return `area`

3. for loop and count

    - each time a new connected component's size is discovered
    - when the size is bigger than the previous one, update `maxarea`


### Complexity Analysis:

Time Complexity: *O(m * n)*

- check all verticies

Space Complexity: *O(m * n)*

- `seen` set

---


### Solution 2: DFS with iterative stack 

```python

"""
same
"""
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

"""
same
"""
```
### Breakdown of Solution:

**Depth First Search (Graph)**

The idea and solution breakdown is identical.

The only difference is the way `dfs()` is constructed. This time, iterative stack is used.


### Complexity Analysis:

Time Complexity: *O(m * n)*

- check all verticies

Space Complexity: *O(m * n)*

- `seen` set