from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> list[int]:
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