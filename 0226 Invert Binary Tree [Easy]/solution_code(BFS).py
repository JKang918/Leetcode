from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    #solution 3. BFS
    
    if not root:
        return root

    queue = deque([root])

    while queue:
        curr_len = len(queue)

        for _ in range(curr_len):
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root