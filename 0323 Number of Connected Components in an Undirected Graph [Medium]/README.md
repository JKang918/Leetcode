## 323. Number of Connected Components in an Undirected Graph

>Description: [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/)\
Check out the link above

Constraints:

- <code>1 <= n <= 2000</code> 
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai <= bi < n`
- `ai != bi`
- There are no repeated edges.


### Solution 1: DFS with recursive function 

```python
from collections import defaultdict

def countComponents(n: int, edges: list[list[int]]) -> int:
    ###preprocessing
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x) #undirected
    
    #isolated vertices
    for i in range(n):
        if i not in graph:
            graph[i] = []
    
    ###preprocessing end

    def dfs(node: int) -> None:
        for neighbor in graph[node]:
            if neighbor not in seen: #to prevent redundant searches
                seen.add(neighbor)   #to prevent redundant searches
                dfs(neighbor)
        return

    
    count = 0 #number of provinces
    seen = set()
    for node in graph:
        #if statement only runs when a node in a new connected component comes in
        if node not in seen:
            seen.add(node)
            count += 1
            dfs(node)
    return count
```
### Breakdown of Solution:

**Depth First Search (Graph)**

The problem is finding the number of connected components.

Whenever a new connected componenet comes up, `count` incremented by one. 


### Complexity Analysis:

Time Complexity: *O(n)*

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
                if neighbor not in seen: #to prevent redundant searches
                    seen.add(neighbor)   #to prevent redundant searches
                    stack.append(neighbor)
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

Time Complexity: *O(n)*

- check all verticies

Space Complexity: *O(n)*

- `seen` set