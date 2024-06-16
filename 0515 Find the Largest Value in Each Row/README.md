## 515. Find the Largest Value in Each Row

>Description: [515. Find the Largest Value in Each Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/editorial/)\
Given the root of a binary tree, return an array of the largest value in each row of the tree **(0-indexed)**.

Constraints:

- The number of nodes in the tree will be in the range <code>[0, 10<sup>4</sup>]</code> .
- <code>-2<sup>31</sup> <= Node.val <= 2<sup>31</sup></code> 

### Solution: 

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
### Breakdown of Solution:

**Breadth First Search**

- BFS implemented using while and inner for loop.
    - while loop iteration for each row
    - for loop iteration for each node in a given row

- while searching through each node in a given row (hence during for loop), update `num` to reflect the maximum node value.
- append the maximum node value to the answer list at the end of each for loop iteration. 

### Complexity Analysis:

Time Complexity: *O(n)*

- check each node

Space Complexity: *O(n)*

- for perfect binary tree, maximum space occupied would be n/2.