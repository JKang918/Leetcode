from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
    if not root:
        root = TreeNode(val)

    if root.val < val:
        root.right = self.insertIntoBST(root.right, val)
    
    if val < root.val:
        root.left = self.insertIntoBST(root.left, val) 
        
    return root