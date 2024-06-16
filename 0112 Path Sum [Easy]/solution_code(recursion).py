# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:

        if not root: return False
        
        #Base case
        if not root.left and not root.right:
            return root.val == targetSum

        left = hasPathSum(root.left, targetSum - root.val)
        right = hasPathSum(root.right, targetSum - root.val)

        return left or right