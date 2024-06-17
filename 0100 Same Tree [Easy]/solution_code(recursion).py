from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #Empty Tree #condition 1 and 2 met: do not exist / no children (identical children)
    if not p and not q:
        return True
    
    #Only one empty
    elif not p or not q:
        return False
    
    #Exist, but different values
    elif p.val != q.val:
        return False
    
    #condition 1 met: exist and same value
    
    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)

    #condition 2 met: children are identical
    return left and right