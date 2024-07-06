## 841. Keys and Rooms

>Description: [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)\
Check out the link above.

Constraints:

- <code>1 <= n <= 1000</code> 
- `n == rooms.length`
- <code>1 <= rooms[i].length <= 1000</code> 
- <code>1 <= sum(rooms[i].length) <= 3000</code> 
- <code>1 <= rooms[i][j] < n</code> 
- All the values of `rooms[i]` are **unique**.


### Solution 1: DFS with recursive function 

```python
def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    
    seen = {0}

    #recursive
    def dfs(start):
        room = start
        for neighbor in rooms[room]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    dfs(0)
    return len(seen) == len(rooms)
```
### Breakdown of Solution:

**Depth First Search (Graph)**


Input is an array of other verticies from the current vertex. No processing required.

Define DFS function, starting from a random vertex, all vertices are reachable then return `True`.

I put down `dfs(0)` but the starting point can be any vertex. 

### Complexity Analysis:

Time Complexity: *O(n)*

- check all verticies

Space Complexity: *O(n)*

- `seen` set

---


### Solution 2: DFS with iterative stack 

```python

def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    
    seen = {0}

    #iterative stack
    stack = [0]

    while stack:
        room = stack.pop()
        for neighbor in rooms[room]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
                
    return len(seen) == len(rooms)
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