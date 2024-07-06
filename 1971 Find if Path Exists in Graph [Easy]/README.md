## 1971. Find if Path Exists in Graph
 
>Description: [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)\
Check out the link for description

Constraints:

- <code>2 <= n <= 2*10<sup>5</sup></code> 
- <code>2 <= endges.length <= 2*10<sup>5</sup></code> 
- `edges[i].length == 2`
- `0 <= ui, vi <= n - 1`
- `0 <= source, destination <= n - 1`
- There are no duplicate edges.
- There are no self edges.


### Solution 1. DFS with recursive function

```python
from collections import defaultdict
def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    
    #number of connected component is 1 -> True

    ###preprocessing
    graph = defaultdict(list)
    #for isolated vertices
    for i in range(n):
        graph[i] = []
    #

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x) #undirected
    ###preprocessing end
    
    #DFS: recursive function
    def dfs(node: int) -> None:
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)
        return
    
    seen = {source}
    dfs(source)

    return destination in seen
```

### Breakdown of Solution 1.:

**Depth First Search (Graph)**

Starting from `source` do depth first search.

If `destination` is added to `seen` return `True`.

### Complexity Analysis:

Time Complexity: *O(n)*

- DFS

Space Complexity: *O(n)*

- `graph`
- stack

---

### Solution 2. DFS with iterative stack

```python
#### same

#DFS: iterative stack
        def dfs(start: int) -> None:
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            return

#### same
```

### Breakdown of Solution 2:

**Depth First Search (Graph)**

The idea and solution breakdown is identical.

The only difference is the way `dfs()` is constructed. This time, iterative stack is used.

### Complexity Analysis:

Time Complexity: *O(n)*

- DFS

Space Complexity: *O(n)*

- `graph`
- stack