## 938. Range Sum of BST

>Description: [938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)\
Given the `root` node of a binary search tree and two integers `low` and `high`, return *the sum of values of all nodes with a value in the **inclusive** range* `[low, high]`.


Constraints:

- The number of nodes in the tree will be in the range <code>[1, 2 * 10<sup>4</sup>]</code> .
- <code>1 <= Node.val <= 10<sup>5</sup></code> 
- <code>1 <= low <= high <= 10<sup>5</sup></code> 
- All `Node.val` are **unique**.



### Solution 1 (DFS with recursion): 

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfsSum(node, ans = 0):
            if not node: return 0

            if low <= node.val <= high:
                ans += node.val
            
            if node.left and low < node.val:
                ans += dfsSum(node.left)
            
            if node.right and node.val < high:
                ans += dfsSum(node.right)
            
            return ans
        
        return dfsSum(root, 0)
```
### Breakdown of Solution 1:

**Depth First Search (recursion)**

- DFS implemented using recursion.
    - recursive relations go on until leaf nodes show up.

The basic idea: only search further down when you have a chance.
- e.g., if node.val <= low, then no point in searching left subtree. Vice versa with the right subtree when node.val >= high.

- Base case
    - At leaf node, check if the node itself meets the condition. No other if statements are run.


### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(height of the tree)*

- Best case: log n
- Worst case: n (chain shaped tree)
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


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    
    if not root: return 0

    ans = 0
    stack = [root]

    while stack:
        node = stack.pop()
        if low <= node.val <= high:
            ans += node.val
        
        if node.left and low < node.val: 
            stack.append(node.left)
        if node.right and node.val < high:
            stack.append(node.right)
    return ans
```
### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

The underlying idea is identical to that of solution 1.\
The only change is the same logic is implemented using stacks directly.

Store `depth` data into the stack along with each corresponding node.


### Complexity Analysis:

Same as solution 1