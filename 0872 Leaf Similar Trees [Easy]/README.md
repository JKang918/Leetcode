## 872. Leaf Similar Trees

>Description: [872. Leaf Similar Trees](https://leetcode.com/problems/leaf-similar-trees/description/)\
Check out the link above

Constraints:

- The number of nodes in each tree will be in the range `[1, 200]`.
- Both of the given trees will have values in the range `[0, 200]`.

### Solution 1: DFS - recursion

```python
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

    #DFS recursive function
    def dfs(treenode, leaf: List) -> None:

        node = treenode

        if not node:
            return 

        if not node.left and not node.right:
            leaf.append(node.val)

        if node.left:
            dfs(node.left, leaf)

        if node.right:
            dfs(node.right, leaf)
        
        return
    
    leaf1 = []
    leaf2 = []
    dfs(root1, leaf1)
    dfs(root2, leaf2)
    return leaf1 == leaf2
```
### Breakdown of Solution:

**Depth First Search (Binary Tree)**

A few notable points in this `dfs` function are below:

1. argument: it takes an empty list as an argument
2. leaf node condition: additional condition when it is a leaf node: Node value is appended to the input list.

So while performing DFS for both trees, leaf nodes are appended to each linked list: `leaf1` and `leaf2`.

Chekc whether they are identical.


### Complexity Analysis:

Time Complexity: *O(T1 + T2)*

- Traverse both trees

Space Complexity: *O(T1 + T2)*

- For leafnodes in both trees

---

### Solution 2: DFS using stack

```python
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


    #DFS: iterative stack

    def dfsStack(treenode):
        leaf = []    
        stack = [treenode]

        while stack:
            node = stack.pop()

            if not node.left and not node.right:
                leaf.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaf
    
    return dfsStack(root1) == dfsStack(root2)
```
### Breakdown of Solution:

**Depth First Search with iterative stack**

Instead of declaring dfs function, we can use iterative stack method to acheive the same outcome.

### Complexity Analysis:

Time Complexity: *O(T1 + T2)*

- Traverse both trees

Space Complexity: *O(T1 + T2)*

- For leafnodes in both trees and the stack