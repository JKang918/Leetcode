## 542. 01 Matrix

>Description: [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)\
Check out the link above.

Constraints:

- `m == mat.length`
- `n == mat[i].length`
- <code>1 <= m, n <= 10<sup>4</sup></code>
- <code>1 <= m * n <= 10<sup>4</sup></code>
- `mat[i][j]` is either `0` or `1`.
- There is at least one `0` in `mat`.


### Solution

```python
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
```
### Breakdown of Solution:

**Bredth First Search (Graph)**

My initial thought was perform BFS for every cell of `1`. But then it would be so inefficient because BFS will be performed unnecessarily too many times.

Instead, do one BFS for every node with `0` would give you the same result. This is because distance from `1` to `0` is equal to distance from `0` to `1`.

In this particular solution, I modifed the input matrix and returned it. But if the problem dictates otherwise, such as the input array should be intact, create new object and work on it.

### Complexity Analysis:

Time Complexity: *O(m * n)*

- check all cells

Space Complexity: *O(n)*

- `seen` set