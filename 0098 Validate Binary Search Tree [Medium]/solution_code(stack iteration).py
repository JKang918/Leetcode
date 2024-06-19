from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    if not root: 
        return True

    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, small, large = stack.pop()

        if not(small < node.val < large):
            return False
        
        else:
            if node.right:
                stack.append((node.right, node.val, large))
            if node.left:
                stack.append((node.left, small, node.val))
            
    return True
