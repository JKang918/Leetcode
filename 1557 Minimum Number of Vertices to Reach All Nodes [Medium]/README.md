## 1577. Minimum Number of Vertices to Reach All Nodes
 
>Description: [1577. Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/)\
Check out the link for description

Constraints:

- <code>2 <= n <= 10<sup>5</sup></code> 
- <code>1 <= edges.length <= min(10<sup>5</sup>, n * (n - 1) / 2)</code> 
- `edges[i].length == 2`
- `0 <= fromi, toi < n`
- All pairs `(fromi, toi)` are distinct.

### Solution

```python
def findSmallestSetOfVertices(n: int, edges: list[list[int]]) -> list[int]:
    
    #find all vertices with indegree of zero
    indegree = [0] * n
    
    for x, y in edges:
        indegree[y] += 1
    
    return [node for node in range(n) if indegree[node] == 0]
```

### Breakdown of Solution:

Understanding that this question is asking you to retreive all the vertices with indegree is `0` is the key.

1. Declare `indegree` python list to store indegree of each vetex
2. for loop: update `indegree`
3. return the index list where `indegree[index] == 0`

### Complexity Analysis:

Time Complexity: *O(n)*

- traverse the input

Space Complexity: *O(n)*

- `indegree`