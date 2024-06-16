## 1448. Count Good Nodes in a Binary Tree

>Description: [1448. Count Good Nodes in a Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)\
Given a binary tree `root`, a node *X* in the tree is named **good** if in the path from root to *X* there are no nodes with a value *greater than* X.\
Return the number of **good** nodes in the binary tree.


Constraints:

- The number of nodes in the tree will be in the range <code>[1, 10<sup>5</sup>]</code> .
- <code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code> 


### Solution 1 (DFS with recursion): 

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node: TreeNode, maxsofar):
        if not node:
            return 0
        cnt = 0
        if node.val >= maxsofar:
            cnt += 1
            maxsofar = node.val
        left = dfs(node.left, maxsofar)
        right = dfs(node.right, maxsofar)
        return left + right + cnt

#solution function
def goodNodes(root: TreeNode) -> int:
    
    return dfs(root, float('-inf'))
```
### Breakdown of Solution 1:

**Depth First Search (recursion)**

- DFS implemented using recursion.
    - recursive relations go on until leaf nodes show up.

The basic idea is simple; add the number of qualifying nodes in the left subtree and the right subtree.

- Base case
    - At leaf node, compare the node value and the maximum value so far in the path to that leaf node.
        - Therefore, store and update the maximum value along the path.
        - At leaf node, `left` and `right` will be `0`. return `0` if itself does not satisfy the condition, elsewise return `1`. 

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
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, maxsofar):
        if not node: return 0
        stack = [(node, maxsofar)]
        cnt = 0
        while stack:
            node, maxsofar= stack.pop()
            if node.val >= maxsofar:
                cnt += 1
                maxsofar = node.val

            if node.right:
                stack.append((node.right, maxsofar))
            if node.left:
                stack.append((node.left, maxsofar))
        return cnt

#solution function
def goodNodes(root: TreeNode) -> int:
    
    return dfs(root, float('-inf'))
```
### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

The underlying idea is identical to that of solution 1.\
The only change is the same logic is implemented using stacks directly.

- Track the maximum value along the path.
- Check a given node value exceeds the maximum value -> if so, add `1` to the count variable.


### Complexity Analysis:

Same as solution 1