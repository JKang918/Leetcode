## 863. All Nodes Distance K in Binary Tree

>Description: [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)\
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


### Solution 1: DFS modify input tree 

```python
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

####################################

def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    
    def dfs(node, parent):
        if not node:
            return
        node.parent = parent
        
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)
    
####################################

    distance = 0
    queue = deque([target])
    seen = {target}

    #distance < k : k-distance nodes only
    while queue and distance < k:
        curr_level = len(queue)
        for _ in range(curr_level):
            node = queue.popleft()
            for neighbor in [node.left, node.right, node.parent]:
                #uncharted node and the tree node exists
                if neighbor not in seen and neighbor:
                    seen.add(neighbor)
                    queue.append(neighbor)
        distance += 1
                
    #array of the k-distance tree node.vals 
    return [node.val for node in queue]    
```
### Breakdown of Solution:

**Depth First Search (Graph)**

```python
def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    
    def dfs(node, parent):
        if not node:
            return
        node.parent = parent
        
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)
```
First, using DFS algorithm, go over all the nodes in a given tree and designate 'parent' pointer to each node.

Then, each node, in terms of graph terminology, will have three neighbors: left child, right child, and parent.

Use BFS from the target node to find and store all the nodes that are k-distance away from the target.

This proble befits BFS more than DFS because distance matters.


### Complexity Analysis:

Time Complexity: *O(n)*

- O(n) for DFS, O(n) for BFS

Space Complexity: *O(n)*

- `seen` set

---


### Solution 2: BFS - input tree intact 

```python
from collections import deque
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

####################################

def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    
    #idea: 1. graph 2. do bfs(graph) from that node

    ###preprocessing: from tree to graph
    graph = defaultdict(list)
    queue = deque([root])

    while queue:
        curr_level = len(queue)
        for i in range(curr_level):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val) #undirected
            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val) #undirected
####################################

    queue = deque([target.val])
    seen = {target.val}
    #ans = []

    #k distance from target
    for j in range(k):
        curr_level = len(queue)
        for n in range(curr_level):
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
    ###end of the outer for loop: queue with k distance nodes
    
    return [node for node in queue]
```
### Breakdown of Solution:

**Breadth First Search (Graph)**

The idea is similar in the second part. Use BFS to find the k-distnace nodes.

Solution 2 complements Solution 1 in that it does not modify the input tree, which is one downside of Solution 1.

Instead, by using BFS, we construct separate defaultdict object, `graph`, from which we perform second BFS to find k-distance nodes.


### Complexity Analysis:

Time Complexity: *O(n)*

- for BFSs

Space Complexity: *O(n)*

- For `graph` and `seen` set