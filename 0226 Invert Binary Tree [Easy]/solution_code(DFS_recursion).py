from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    #solution 1. recursion
    def dfs(node) -> None:
        if not node:
            return
        node.left, node.right = node.right, node.left

        dfs(node.left)
        dfs(node.right)
        return
    
    dfs(root)
    return root