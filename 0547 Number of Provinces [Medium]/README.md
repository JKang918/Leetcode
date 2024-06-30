## 547. Number of Provinces

>Description: [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)\
There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.\
A province is a group of directly or indirectly connected cities and no other cities outside of the group.\
You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.\
Return the total number of provinces.

Constraints:

- <code>1 <= n <= 200</code> 
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j] is 1 or 0.`
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`


### Solution 1: DFS with recursive function 

```python
from collections import defaultdict

def findCircleNum(isConnected: list[list[int]]) -> int:
    ###preprocessing
    graph = defaultdict(list)

    ##becuase of isolated vertices
    for i in range(len(isConnected)):
        graph[i] = []

    for i in range(len(isConnected) - 1):
        for j in range(i+1, len(isConnected[0])):
            if isConnected[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i) #undirected
    ###preprocessing end
    
    def dfs(vtx: int) -> None:
        for neighbor in graph[vtx]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)
        return 
    
    seen = set()
    count = 0
    for vtx in graph:
        if vtx not in seen:
            seen.add(vtx)
            dfs(vtx)
            count += 1
    return count
```
### Breakdown of Solution:

**Depth First Search (Graph)**

Input matrix: each element in a matrix represents each edge in a graph

graph hash map from the input matrix: undirected edges

Meaning of Number of Provinces: Number of connected components

This problem is asking you to get the number of connected components in a given graph, which is suited for DFS approach.

The only thing to take note of here is how DFS is implemented.

1. `dfs()` function

    - if there is a connected neighboring vertex ( = connected), then call the recursive function, `dfs()`

2. for loop and count

    - each time a new connected component is discovered ( = new vertex not in `seen` is discovered), increment `count` by one


### Complexity Analysis:

Time Complexity: *O(n * n)*

- check all verticies

Space Complexity: *O(n)*

- `seen` set

---


### Solution 2: DFS with iterative stack 

```python

"""
same
"""
    def dfs(start: int) -> None:
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
"""
same
"""
```
### Breakdown of Solution:

**Depth First Search (Graph)**

The idea and solution breakdown is identical.

The only difference is the way `dfs()` is constructed. This time, iterative stack is used.


### Complexity Analysis:

Time Complexity: *O(n * n)*

- check all verticies

Space Complexity: *O(n)*

- `seen` set