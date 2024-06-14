## 2352. Equal Row and Column Pairs

>Description: [2352. Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/)\
Given a **0-indexed** `n x n` integer matrix `grid`, return the number of pairs `(ri, cj)` such that row `ri` and column `cj` are equal.\
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


Constraints:

- <code>1 <= n <= 200</code> 
- <code>1 <= grid[i][j] <= 10<sup>5</sup>/</code>
- `n == grid.length == grid[i].length`


### Solution: 

```python
def equalPairs(grid: list[list[int]]) -> int:
    
    rowcount = dict()
    #grid: matrix with row colums
    """
    [[....],
     [....],
     ...
     [....]
    ]
    """

    for i in range(len(grid)):
        #list is unhashable
        #for each row, count
        #if there is multiple same rows -> that multipilicity is stored as dictionary.values
        rowcount[tuple(grid[i])] = rowcount.get(tuple(grid[i]), 0) + 1  
    
    ans = 0
    for j in range(len(grid)):
        #construct column vectors from a given grid
        col = []
        for k in range(len(grid)):
            col.append(grid[k][j])
        
        #add the count of row vectors identical to each column vectors
        ans += rowcount.get(tuple(col), 0)

    return ans
```

### Breakdown of Solution:

**Hash table**

Use the row vectors as key and the frequency of them as values.

Construct column vectors.

Check how many identical row vectors are there for a given column vector.

### Complexity Analysis:

Time Complexity: *O(n^2)*

- nested for loop to construct column vectors

Space Complexity: *O(n)*

- storing `rowcount`
