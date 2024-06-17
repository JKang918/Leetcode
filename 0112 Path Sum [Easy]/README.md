## 112. Path Sum

>Description: [112. Path Sum](https://leetcode.com/problems/path-sum/)\
Given the `root` of a binary tree and an integer `targetSum`, return true if the `tree` has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.\
For detailed example cases, please check out the above links.

Constraints:

- The number of nodes in the tree will be in the range <code>[0, 10<sup>4</sup>]</code> .
- <code>-10<sup>2</sup> <= Node.val <= 10<sup>2</sup></code> 


### Solution 1 (DFS with recursion): 

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:

        if not root: return False
        
        #Base case
        if not root.left and not root.right:
            return root.val == targetSum

        left = hasPathSum(root.left, targetSum - root.val)
        right = hasPathSum(root.right, targetSum - root.val)

        return left or right  
```
### Breakdown of Solution 1:

**Depth First Search (recursion)**

- DFS implemented using recursion.
    - recursive relations go on until leaf nodes show up.

The basic idea is simple; targetsum problem reapeats in subtrees so use recursion

- Base case
    - At leaf node, the node value itself shoud be equal to the (adjusted) `targetSum`.
    - at the parent node of a given leaf node, if such leaf node exists then return `True`.


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
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:

    if not root: return False
    
    stack = [(root, 0)]
    
    while stack:
        node, cumulsum = stack.pop()
        cumulsum += node.val
        
        if not node.right and not node.left:
            if cumulsum == targetSum: return True
        
        if node.right:
                stack.append((node.right, cumulsum))
        if node.left:
                stack.append((node.left, cumulsum))
```
### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

The underlying idea is identical to that of solution 1.\
The only change is the same logic is implemented using stacks directly.

- Track cumulative sum data
- If at leaf node, the cumulative sum meets the `targetSum`, return `True`


### Complexity Analysis:

Same as solution 1