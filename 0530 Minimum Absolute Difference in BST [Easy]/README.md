## 530. Minimum Absolute Difference in BST

>Description: [530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/submissions/)\
Given the `root` of a Binary Search Tree (BST), return *the minimum absolute difference between the values of any two different nodes in the tree*.


Constraints:

- The number of nodes in the tree will be in the range <code>[2, 10<sup>4</sup>]</code> .
- <code>0 <= Node.val <= 10<sup>5</sup></code> 


### Solution 1 (DFS with recursion): 

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#depth first search - inorder
def dfs(node, values):
    if not node: return
    
    if node.left:
        dfs(node.left, values)
    
    #inorder beg
    values.append(node.val)
    #inorder end

    if node.right:
        dfs(node.right, values)
    
    return values

def getMinimumDifference(root: Optional[TreeNode]) -> int:
    
    values = list()
    dfs(root, values)
    diff = float('inf')
    for i in range(0, len(values) - 1):
        diff = min(diff, values[i + 1] - values[i])
        if diff == 1: return 1
    return diff
```
### Breakdown of Solution 1:

**Depth First Search (recursion)**

- DFS (inorder) implemented using recursion.
- **DFS (inorder) & BST ==> sorted array** -> This is the key point in this problem
- Find the min abs diff between elements in a sorted array, `values`.
- The smallest abs diff is `1`. So luckily, during iteration when `1` shows up just return that one.

### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(n)*

- store all nodes
    
---

### Solution 2 (DFS with iterative stack): 

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
        stack = []
        values = []
        curr = root

        # when no "or curr", it only searchs the left subtree from the root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                #inorder beg
                values.append(curr.val)
                #inorder end
                curr = curr.right
        
        return values


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    
    value = list()
    dfs(root, value)
    diff = float('inf')
    for i in range(0, len(value) - 1):
        diff = min(diff, value[i + 1] - value[i])
        if diff == 1: return 1
    return diff
```
### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

The underlying idea is identical to that of solution 1.\
The only change is the same logic is implemented using stacks directly.

Note that inorder DFS with stack iteration looks a bit tricker. Unlike preorder DFS, "or curr" condition is added to the while loop.

### Complexity Analysis:

Same as solution 1