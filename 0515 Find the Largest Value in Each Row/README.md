## 515. Find the Largest Value in Each Row

>Description: [515. Find the Largest Value in Each Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/editorial/)\
Given the root of a binary tree, return an array of the largest value in each row of the tree **(0-indexed)**.

Constraints:

- The number of nodes in the tree will be in the range <code>[0, 10<sup>4</sup>]</code> .
- <code>-2<sup>31</sup> <= Node.val <= 2<sup>31</sup></code> 

### Solution 1 (Breadth First Search): 

```python
#To use Deque (data structure)
from collections import deque  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Breadth First Search using Queue and iteration
def largestValues(root: TreeNode) -> list[int]:
    #Empty Tree
    if not root: return []
    
    #Otherwise: Nonempty cases
    queue = deque()
    queue.append(root)

    #to store highest values in each row
    ans = list()        
    
    while queue:
        
        #level length
        lvllen = len(queue)
        
        #-2^(31) is the smallest possible value for nodes #check the constraint above
        num = -2**31            
        
        # iteration for the length of the given row (level)
        for i in range(lvllen):
            node = queue.popleft()
            #to store the maximum node value in a given row
            num = max(num, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # after each for loop, which covers all nodes on the same row, add the max node value to the list
        ans.append(num)
    return ans
```
### Breakdown of Solution 1:

**Breadth First Search**

- BFS implemented using while and inner for loop.
    - while loop iteration for each row
    - for loop iteration for each node in a given row

- while searching through each node in a given row (hence during for loop), update `num` to reflect the maximum node value.
- append the maximum node value to the answer list at the end of each for loop iteration. 

### Complexity Analysis (Solution 1):

Time Complexity: *O(n)*

- check each node

Space Complexity: *O(n)*

- for perfect binary tree, maximum space occupied would be n/2.




### Solution 2 (Depth First Search): 

```python
#To use Deque (data structure)
from collections import deque  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root: TreeNode) -> list[int]:
    ans = []

    #DFS function define
    def dfs(node, depth): 
        if not node:
            return []
        
        #Store the first node value (from left)  in each row
        if len(ans) == depth:
            ans.append(node.val)
        
        #Otherwise, update the node value if it is greater than the preeixisting one
        else:
            ans[depth] = max(ans[depth], node.val)
        
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
        return ans
    
    return dfs(root, 0)
```
### Breakdown of Solution 1:

**Depth First Search**

- DFS implemented using recursion.
    - recursive relations go on until leaf nodes appear

- The first node with corresponding `depth` gets appended to the answer list.
- If other nodes with corresponding `depth` have greater node values, the list is updated. 

### Complexity Analysis (Solution 1):

Time Complexity: *O(n)*

- check each node

Space Complexity: *O(h)*

- The maximum depth would be the size of call stack.
- In worst cases, it would be O(n) where the tree looks like a linked list.