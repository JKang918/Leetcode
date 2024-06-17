from typing import Optional

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    if root.left and not root.right:
        left = minDepth(root.left)
        return left + 1
    
    elif root.right and not root.left:
        right = minDepth(root.right)
        return right + 1
    else:            
        left = minDepth(root.left)
        right = minDepth(root.right)
        return min(left, right) + 1