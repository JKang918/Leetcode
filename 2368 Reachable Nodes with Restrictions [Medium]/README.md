## 2368. Reachable Nodes With Restrictions

>Description: [2368. Reachable Nodes With Restrictions](https://leetcode.com/problems/reachable-nodes-with-restrictions/)\
Check out the link above.

Constraints:

- <code>1 <= n <= 10^5</code> 
- `edges.length = n-1`
- `edges[i].length == 2`
- `0 <= ai <= bi < n`
- `ai != bi`
- `edges` represent valid tree
- `1 <= restricted.length < n`
- `1 <= restricted[i] < n`
- All the values of restricted are unique.


### Solution 1: DFS with recursive function 

```python
from collections import defaultdict


def reachableNodes(n: int, edges: list[list[int]], restricted: list[int]) -> int:
    
    ###preprocesscing
    graph = defaultdict(list)
    
    for i in range(n):
        graph[i] = []
    
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    restricted = set(restricted)
    ###preprocessing end


    #DFS: recursive
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen and neighbor not in restricted:
                seen.add(neighbor)
                dfs(neighbor)
        return

    seen = {0}
    dfs(0)

    return len(seen)
```
### Breakdown of Solution:

**Depth First Search (Graph)**

This problem asks you to perform simple depth first search except there are some restricted edges that you cannot use.

Add those restricted edges in `restricted` and use that as a group of edges that are restricted to DFS. 

Start with vertex `0`

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
    #DFS: stack
    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted:
                    seen.add(neighbor)
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

Time Complexity: *O(n * n)*

- check all verticies

Space Complexity: *O(n)*

- `seen` set