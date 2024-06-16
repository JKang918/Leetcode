## 199. Binary Tree Right Side View

>Description: [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)\
Given the `root` of a binary tree, imagine yourself standing on **the right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

Constraints:

- The number of nodes in the tree will be in the range <code>[0, 10<sup>2</sup>]</code> .
- <code>-10<sup>2</sup> <= Node.val <= 10<sup>2</sup></code> 


### Solution: 

```python
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode) -> list[int]:
    #If empty node
    if not root: return []
    #Otherwise: nonempty cases
    queue = deque([root])
    #To store the right side view
    ans = list()
    while queue:
        lvllen = len(queue)
        for i in range(lvllen):
            node = queue.popleft()
            
            #only add to the answer list the rightmost node's value
            if i == (lvllen - 1):
                ans.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
```
### Breakdown of Solution:

**Breadth First Search**

- BFS implemented using while and inner for loop.
    - while loop iteration for each row
    - for loop iteration for each node in a given row

- while searching through each node in a given row (hence during for loop), popleft a node vale *only at the last iteration of for loop*.
    - This node represents the rightmost node in each row 

### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(n)*

- For perfect binary tree, the max queue size would be n/2.
- In worst case, n.
- Either way, O(n) complextiy
    
