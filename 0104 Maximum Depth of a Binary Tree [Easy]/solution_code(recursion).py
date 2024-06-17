from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right) + 1