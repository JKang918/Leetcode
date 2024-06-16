#To use Deque (data structure)
from collections import deque  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root: TreeNode) -> list[int]:
    if not root: return []
    queue = deque()
    queue.append(root)
    ans = list()
    while queue:
        
        lvllen = len(queue)
        #-2^(31) is the smallest possible value for nodes 
        num = -2**31            
        for i in range(lvllen):
            node = queue.popleft()
            num = max(num, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(num)
    return ans