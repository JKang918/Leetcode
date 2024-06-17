from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    
    if not root: return 0

    ans = 0
    stack = [root]

    while stack:
        node = stack.pop()
        if low <= node.val <= high:
            ans += node.val
        
        if node.left and low < node.val: 
            stack.append(node.left)
        if node.right and node.val < high:
            stack.append(node.right)
    return ans