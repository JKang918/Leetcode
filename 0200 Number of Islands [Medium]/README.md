## 200. Number of Islands

>Description: [200. Number of Provinces](https://leetcode.com/problems/number-of-islands/)\
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.\
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:

- `m == grid.length`
- `n == grid[i].length`
- <code>1 <= m, n <= 300</code> 
- `grid[i][j]` is `'0'` or `'1'`.


### Solution 1: DFS with recursive function 

```python
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
```
### Breakdown of Solution:

**Depth First Search (Graph)**

Input matrix: each element in a matrix represents each vertex in a graph

Meaning of Islands: connected in the four dirctions(up, down, left, right) -> connected components

Meaning of Number of Islands: Number of connected components

This problem is asking you to get the number of connected components in a given graph, which is suited for DFS approach.

The only thing to take note of here is how DFS is implemented.

1. `isValid()` function

    - It is to simplify the process of finding connected vertices to a given vertex.
    - If a neighboring vertex is `"1"` then this is connected.

2. `dfs()` function

    - if a neighboring vertex is valid ( = connected), then call the recursive function, `dfs()`

3. for loop and count

    - each time a new connected component is discovered ( = new grid not in `seen` is discovered), increment `count` by one


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
    def dfs(row: int, col: int) -> None:
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            for dx, dy in directions:
                if isValid(r + dx, c + dy) and (r + dx, c + dy) not in seen:
                    seen.add((r + dx, c + dy))
                    stack.append((r + dx, c + dy))
        return

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