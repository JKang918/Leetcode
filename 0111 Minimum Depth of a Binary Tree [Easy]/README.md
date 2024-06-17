## 111. Minimum Depth of a Binary Tree

>Description: [111. Minimum Depth of a Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)\
Given a binary tree, find its minimum depth.\
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Constraints:**

- The number of nodes in the tree will be in the range <code>[0, 10<sup>5</sup>]</code> .
- <code>-10<sup>3</sup> <= Node.val <= 10<sup>3</sup></code> 


### Solution (DFS with recursion): 

```python
from typing import Optional

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    if root.left and not root.right:
        left = minDepth(root.left)
        return left + 1
    
    elif root.right and not root.left:
        right = minDepth(root.right)
        return right + 1
    else:            
        left = minDepth(root.left)
        right = minDepth(root.right)
        return min(left, right) + 1
```
### Breakdown of Solution:

**Depth First Search (recursion)**


- DFS implemented using recursion.
    - recursive relations go on until leaf nodes show up.

The basic idea is simple; a min depth of a tree is the lesser of the depth of the left subtree and the right subtree, and then add `1` to it.

In this respect, it bears close resemblance to the below problem:

- [104. Maximum Depth of a Binary Tree - ReadMe.md](https://github.com/JKang918/Leetcode/blob/ba57412a1de470ecde83f6b1db1e8dfebcf87d26/0104%20Maximum%20Depth%20of%20a%20Binary%20Tree%20%5BEasy%5D/README.md)\

However, unlike getting the maximum depth, there are few more considerations:
- When only one of the subtrees exist: we need to take our path down to the existing subtree.
- In the maximum case, we did not have to take this account as we were only interested in the max depth: if a subtree doesn't exist, the depth of it would be zero and will be ignored in `max()` function.

Therefore, in case of only one subtree existing at a given node, we do not apply `min()` function.



### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(log(n))*

- For perfect binary tree, the max stack call size would be log(n).
- In worst case, n.