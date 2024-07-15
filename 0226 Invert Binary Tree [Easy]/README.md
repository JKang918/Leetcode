## 226. Inverted Binary Tree

>Description: [226. Inverted Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)\
Given the `root` of a binary tree, invert the tree, and return its root.

Constraints:

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

### Solution 1: DFS - recursion

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    #solution 1. recursion
    def dfs(node) -> None:
        if not node:
            return
        
        #This is added to ivert left and right subtrees
        node.left, node.right = node.right, node.left
        #

        dfs(node.left)
        dfs(node.right)
        return
    
    dfs(root)
    return root
```
### Breakdown of Solution:

**Depth First Search (Graph)**

Declare `dfs` function to perform DFS. From the template DFS function format, one more line is added:

```python
        #This is added to ivert left and right subtrees
        node.left, node.right = node.right, node.left
        #
```

Other than that, all the rest simple.

Perform DFS and at each and every node, invert the right and left subtrees.


### Complexity Analysis:

Time Complexity: *O(n)*

- O(n) for DFS

Space Complexity: *O(n)*

- For stack

---

### Solution 2: DFS using stack

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    #solution 2. DFS-iterative stack
    if not root:
        return root
    
    stack = [root]
    
    while stack:
        node = stack.pop()

        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return root
```
### Breakdown of Solution:

**Depth First Search**

Instead of declaring dfs function, we can use iterative stack method to acheive the same outcome.

### Complexity Analysis:

Time Complexity: *O(n)*

- for DFS

Space Complexity: *O(n)*

- For stack

---


### Solution 3: BFS using deque

```python
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    #solution 3. BFS
    
    if not root:
        return root

    queue = deque([root])

    while queue:
        curr_len = len(queue)

        for _ in range(curr_len):
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root
```
### Breakdown of Solution:

**Breadth First Search**

The same can be aceived using BFS. Do the inversion at every node but this time, it is BFS.

### Complexity Analysis:

Time Complexity: *O(n)*

- for BFSs

Space Complexity: *O(n)*

- For queue