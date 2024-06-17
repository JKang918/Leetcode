from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfsSum(node, ans = 0):
            if not node: return 0

            if low <= node.val <= high:
                ans += node.val
            
            if node.left and low < node.val:
                ans += dfsSum(node.left)
            
            if node.right and node.val < high:
                ans += dfsSum(node.right)
            
            return ans
        
        return dfsSum(root, 0)