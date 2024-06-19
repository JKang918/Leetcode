## 98. Valid Binary Search Tree

>Description: [98. Valid Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)\
Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.\
A **valid BST** is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Constraints:

- The number of nodes in the tree will be in the range <code>[1, 10<sup>4</sup>]</code> .
- <code>-2<sup>31</sup> <= Node.val <= 2<sup>31</sup></code> 


### Solution 1 (recursive DFS function): 

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, small, large):
        if not node: 
            return True

        if not (small < node.val < large):
            return False
        
        left = dfs(node.left, small, node.val)
        right = dfs(node.right, node.val, large)
        return left and right
    
    return dfs(root, float('-inf'), float('inf'))

```
### Breakdown of Solution 1:

**Depth First Search (recursion)**

- DFS implemented using recursion.
    - recursive relations go on until leaf nodes show up.

At a certain node:
1. node.val itself should meet the condition
2. left child should meet the condtion
3. right chidl should meet the conditon

Hence, perfect example to implement recursive function to get the desired result.
So below lines were added.

```python
if not (small < node.val < large):
            return False
        
        left = dfs(node.left, small, node.val)
        right = dfs(node.right, node.val, large)
        return left and right
```

At the base:
1. leaf nod.val itself should meet the condition
2. need to make it that the left child (None) should result in True
3. need to make it that the right child (None) should result in True

So below lines were added.

```python
    if not node: 
        return True
```

Lastly, at the beginning, root.val is the starting point so always meet the condition 1. So we set the initial `small` and `large` infinite values.


### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(log(n))*

- For perfect binary tree, the max stack call size would be log(n).
- In worst case, n.
    
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

def isValidBST(root: Optional[TreeNode]) -> bool:
    if not root: 
        return True

    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, small, large = stack.pop()

        if not(small < node.val < large):
            return False
        
        else:
            if node.right:
                stack.append((node.right, node.val, large))
            if node.left:
                stack.append((node.left, small, node.val))
            
    return True

```
### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

The underlying idea is identical to that of solution 1.\
The only change is the same logic is implemented using stacks directly.


### Complexity Analysis:

Same as solution 1