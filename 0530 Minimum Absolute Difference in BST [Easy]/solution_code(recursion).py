from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#depth first search - inorder
def dfs(node, values):
    if not node: return
    
    if node.left:
        dfs(node.left, values)
    
    #inorder beg
    values.append(node.val)
    #inorder end

    if node.right:
        dfs(node.right, values)
    
    return values

def getMinimumDifference(root: Optional[TreeNode]) -> int:
    
    values = list()
    dfs(root, values)
    diff = float('inf')
    for i in range(0, len(values) - 1):
        diff = min(diff, values[i + 1] - values[i])
        if diff == 1: return 1
    return diff