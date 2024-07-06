## 1466. Reorder Routes

>Description: [1466. Reorder Routes](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)\
Check out the link for description

Constraints:

- <code>2 <= n <= 5 * 10<sup>4</sup></code> 
- `connections.length == n - 1`
- `connections[i].length == 2`
- `0 <= ai, bi <= n - 1`
- `ai != bi`

### Solution 1: DFS with recursive function 

```python
from collections import defaultdict

def minReorder(self, n: int, connections: list[list[int]]) -> int:
    ###preprocessing (assume undirected)
    graph = defaultdict(list)

    #no isolated virtex

    route = set()

    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x) #undirected 
        route.add((x, y))  #to check edges #original direction information only

    ###preprocessing end
    
    
    #dfs: traverse away from "0"
    def dfs(node: int):
        ans = 0
        for neighbor in graph[node]:
            if neighbor not in seen:
                ### check whether the original direction is going away from "0"
                if (node, neighbor) in route: 
                    ans += 1
                ###
                seen.add(neighbor)
                ans += dfs(neighbor)
        return ans
        
    seen = {0}
    
    return dfs(0)
```
### Breakdown of Solution:

**Depth First Search (Graph)**

Input is a list of edges.

We preprocess this input and get the graph in the form of hash map.\

Although the given edges are directed, treat the whole graph as undirected during preprocessing. Instead, declare a set to store the original directions information.

Given by the problem condition that it is **guaranteed** every vertex can reach vertex `0` after reorder, all vertices are reachable from `0` in our `graph` using function `dfs`.

Because the traversal is away from `0`, whenever the edge is found in `route`, the set storing the original direction, we can see that this is the edge that need to be swapped. 


### Complexity Analysis:

Time Complexity: *O(n)*

- preprocessing: O(n)
- traversal: O(n)
- swap: O(e) s.t. e is the number of edges being swapped

Space Complexity: *O(n)*

- hash map
- stack

---


### Solution 2: DFS with iterative stack 

```python

"""
same
"""
    #dfs: traverse away from "0"
        def dfs(node: int):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    ### check whether the original direction is going away from "0"
                    if (node, neighbor) in route: 
                        ans += 1
                    ###
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans
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

- preprocessing: O(n)
- traversal: O(n)
- swap: O(e) s.t. e is the number of edges being swapped

Space Complexity: *O(n)*

- hash map
- stack