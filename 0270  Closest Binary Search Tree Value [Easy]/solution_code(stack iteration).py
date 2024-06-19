from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root: Optional[TreeNode], target: float) -> int:
    def dfs(node):
        if not node: return
        values = []    
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                ###inorder beg
                values.append(curr.val)
                ###inorder end
                curr = curr.right
        return values
    
    
    values = dfs(root)
    return min(values, key = lambda x: abs(x - target))
