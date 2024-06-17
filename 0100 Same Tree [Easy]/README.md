## 100. Same Tree

>Description: [100. Same Tree](https://leetcode.com/problems/same-tree/)\
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.\
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Constraints:

- The number of nodes in the tree will be in the range <code>[0, 10<sup>2</sup>]</code> .
- <code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code> 


### Solution (DFS with recursion): 

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #Empty Tree #condition 1 and 2 met: do not exist / no children (identical children)
    if not p and not q:
        return True
    
    #Only one empty
    elif not p or not q:
        return False
    
    #Exist, but different values
    elif p.val != q.val:
        return False
    
    #condition 1 met: exist and same value
    
    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)

    #condition 2 met: children are identical
    return left and right
```
### Breakdown of Solution:

**Depth First Search (recursion)**

The basic idea is simple;

1. To corresponding nodes should either both nonexistent or existent && hold same values.
2. Their children shoud meet condition 1.

- Base case
    - At corresponding leaf nodes (or if one is nonexistent, where it should have been if it were existent), if their values are same then `left` and `right` would be both `True` (due to first *if statement* for their children, which are nonexistent).


### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(log(n))*

- For perfect binary tree, the max stack call size would be log(n).
- In worst case, n.