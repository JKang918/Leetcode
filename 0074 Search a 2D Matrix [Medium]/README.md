## 71. Simplify Path

>Description: [71. Simplify Path](https://leetcode.com/problems/search-a-2d-matrix/)\
Check out the link above


Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- <code>-10<sup>4</sup> <= matrix[i][j], target <= 10<sup>4</sup></code> 


### Solution: 

```python
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right :
        mid = (left + right) // 2
        r = mid // n
        c = mid % n

        if matrix[r][c] > target:
            right = mid - 1
        
        elif matrix[r][c] < target:
            left = mid + 1
        
        else: #matrix[r][c] == target:
            return True
    
    return False
```
### Breakdown of Solution:

**Binary Search**

As values are already sorted in ascending order, binary search would be a very powerful approach to this problem.

Although the input is 2D array, treat it like a 1D array with quotient and remainder operations.

The whole structure of the solution is typical binary search.

### Complexity Analysis:

Time Complexity: *O(log(m*n))*

- binary search

Space Complexity: *O(1)*

- constants only
