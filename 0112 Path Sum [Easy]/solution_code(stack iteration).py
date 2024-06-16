# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:

    if not root: return False
    
    stack = [(root, 0)]
    
    while stack:
        node, cumulsum = stack.pop()
        cumulsum += node.val
        
        if not node.right and not node.left:
            if cumulsum == targetSum: return True
        
        if node.right:
                stack.append((node.right, cumulsum))
        if node.left:
                stack.append((node.left, cumulsum))
            
            