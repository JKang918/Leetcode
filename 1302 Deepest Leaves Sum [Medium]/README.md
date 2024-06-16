## 1302. Deepest Leaves Sum

>Description: [1302. Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/submissions/)\
Given the `root` of a binary tree, return *the sum of values of its deepest leaves*.
For detailed example cases, please check out the above links.

Constraints:

- The number of nodes in the tree will be in the range <code>[0, 10<sup>4</sup>]</code> .
- <code>1 <= Node.val <= 10<sup>2</sup></code> 


### Solution 1 (BFS): 

```python
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: TreeNode) -> int:
        next_level = deque()
        next_level.append(root)

        while next_level:
            curr_level = next_level
            next_level = deque()
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        ans = 0
        for node in curr_level:
            ans += node.val
        
        return ans
```
### Breakdown of Solution 1:

**Breadth First Search**

- BFS implemented using while and inner for loop.
    - while loop iteration for each row
    - for loop iteration for each node in a given row

- Nodes of interest are the ones on the bottom row; all the rest are irrelevant.
- At the end of while loop, the deque, `curr_level`, contains the nodes of the bottom row.
    - Add the node values in it. 


### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(n)*

- For perfect binary tree, the max stack call size would be n/2.
    
---

### Solution 2 (DFS with iterative stack): 

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(self, root: TreeNode) -> int:   
    curr_depth = 0
    deepest_depth = curr_depth
    deepest_sum = 0
    stack = [(root, 0)]

    while stack:

        node, curr_depth = stack.pop()

        #Leaf node
        if not node.right and not node.left: 
            #if leaf node's depth(curr_depth) is the newest record
            if deepest_depth < curr_depth:
                deepest_depth = curr_depth #update deepest_depth
                deepest_sum = node.val #start adding values
            
            #if leaf node's depth(curr_depth) reaches the deepest_depth so far
            elif deepest_depth == curr_depth:
                deepest_sum += node.val #add the value to the preexisting sum
        
        #non leaf case
        else:
            if node.right:
                stack.append((node.right, curr_depth + 1))
            if node.left:
                stack.append((node.left, curr_depth + 1))
    
    return deepest_sum
        
```
### Breakdown of Solution 2:

**Depth First Search (iterative stack)**

- DFS implemented using iterative stack.

- We only care nodes that meets the below two conditions:
    1. leaf node
    2. deepest level

- Therefore information about the depth should be passed along. Also, algorithms to check whether current depth is the deepest depth should be in place.

1. First **if statement** is to check whether a node is a leaf node.
2. Inner **if, elif statements** are to check whether it is a deeper leaf node than previous deepest leaf node.
    1) if so, update the sum value again. And update the deepest level.
    2) if not, add it to the cumulative sum of leaf nodes at the deepest level(so far).
3. If not leaf node: dig deeper


### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(height of the tree)*

- For perfect binary tree, the max stack call size would be log(n).
- Worst case: height = n
    