## 701. Insert into a Binary Search Tree

>Description: [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)\
You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return *the root node of the BST after the insertion*. It is **guaranteed** that the new value does not exist in the original BST.

Constraints:

- The number of nodes in the tree will be in the range <code>[1, 10<sup>4</sup>]</code> .
- <code>-10<sup>8</sup> <= Node.val <= 10<sup>8</sup></code> 
- All the values `Node.val` are **unique**.
- It's **guaranteed** that `val` does not exist in the original BST.


### Solution 1 (recursive DFS function): 

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
    if not root:
        root = TreeNode(val)

    if root.val < val:
        root.right = self.insertIntoBST(root.right, val)
    
    if val < root.val:
        root.left = self.insertIntoBST(root.left, val) 
        
    return root
```
### Breakdown of Solution 1:

**Depth First Search (recursion)**

- DFS implemented using recursion.
    - recursive relations go on until leaf nodes show up.

At a certain node:
1. check if a given `val` is smaller or greater than the `node.val`
2. if smaller: pick the left subtree and repeat 1.
3. if greater: pick the right subtree and repeat 1.

At the base (leaf node):
1. check if a given `val` is smaller or greater than the `leaf_node.val`
2. if smaller: append to the tree as the leaf node's left child
3. if smaller: append to the tree as the leaf node's right child

Lastly, return `root` because we need to return the updated tree as a whole.

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

def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
    if not root:
        root = TreeNode(val)
        return root
    
    stack = [root]

    while stack:
        node = stack.pop()

        if val < node.val:
            if node.left:
                stack.append(node.left)
            else:
                node.left = TreeNode(val)
                return root
        if node.val < val:
            if node.right:
                stack.append(node.right)
            else:
                node.right = TreeNode(val)
                return root

```
### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

The underlying idea is identical to that of solution 1.\
The only change is the same logic is implemented using stacks directly.


### Complexity Analysis:

Same as solution 1