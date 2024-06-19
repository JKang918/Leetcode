## 270. Closest Binary Search Tree Value

>Description: [270. Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)\
Given the `root` of a binary search tree and a `target` value, *return the value in the BST that is closest to the* `target`. If there are multiple answers, print the smallest.

Constraints:

- The number of nodes in the tree will be in the range <code>[1, 10<sup>4</sup>]</code> .
- <code>0 <= Node.val <= 10<sup>9</sup></code> 
- <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code> 


### Solution 1 (recursive DFS function): 

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root: Optional[TreeNode], target: float) -> int:
    def dfs(node):
        if not node:
            return
        if node.left:
            dfs(node.left)
        #inorder beg
        values.append(node.val)
        #inorder end
        if node.right:
            dfs(node.right)
        return values
    
    values = []
    dfs(root)
    
    return min(values, key = lambda x: abs(x - target))
```
### Breakdown of Solution 1:

**Depth First Search (recursion)**

- DFS implemented using recursion.
    - recursive relations go on until leaf nodes show up.

The logic is simple:
1. Recall that BST with DFS inorder searchs node values in ascending order (smallest to largest)
2. So the list, `values` at the end becomes a sorted array.
3. Use lambda function to obtain the closest node to the target.

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

def closestValue(root: Optional[TreeNode], target: float) -> int:
    def dfs(node):
        if not node: return
        values = []    
        stack = []
        curr = root
        #if no "or curr" it only searches the left subtree
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                ###inorder beg
                values.append(curr.val)
                ###inorder end
                curr = curr.right
        return values
    
    
    values = dfs(root)
    return min(values, key = lambda x: abs(x - target))
```

### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

The underlying idea is identical to that of solution 1.\
The only change is the same logic is implemented using stacks directly.

DFS inorder with stack is more difficult to implement than DFS preorder.


### Complexity Analysis:

Same as solution 1