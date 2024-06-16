## 104. Maximum Depth of a Binary Tree

>Description: [104. Maximum Depth of a Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)\
Given the `root` of a binary tree, return *its maximum depth*.\
A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**
![Example 1](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)
**Input: root** = [3,9,20,null,null,15,7]\
**Output**: 3

**Example 2:**

**Input: root** = [1,null,2]\
**Output**: 2
 

Constraints:

- The number of nodes in the tree will be in the range <code>[0, 10<sup>4</sup>]</code> .
- <code>-10<sup>2</sup> <= Node.val <= 10<sup>2</sup></code> 


### Solution 1 (DFS with recursion): 

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right) + 1
```
### Breakdown of Solution 1:

**Depth First Search (recursion)**

- DFS implemented using recursion.
    - recursive relations go on until leaf nodes show up.

The basic idea is simple; a max depth of a tree is the greater of the depth of the left subtree and the right subtree, and then add 1 to it.

- Base case
    - At leaf node, `left` and `right` would be both zero, hence the depth would be 1.


### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(log(n))*

- For perfect binary tree, the max stack call size would be log(n).
- In worst case, n.
    
---

### Solution 2 (DFS with iterative stack): 

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    stack = [(root, 0)]
    ans = 0
    while stack:
        node, depth = stack.pop()
        ans = max(depth, ans)
        if node.right:
            stack.append((node.right, depth + 1))

        if node.left:
            stack.append((node.left, depth + 1))
    return ans + 1
```
### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

The underlying idea is identical to that of solution 1.\
The only change is the same logic is implemented using stacks directly.

Store `depth` data into the stack along with each corresponding node.
Return the maximum `depth`. Add `1` to adjust for **0-indexing**.  


### Complexity Analysis:

Same as solution 1