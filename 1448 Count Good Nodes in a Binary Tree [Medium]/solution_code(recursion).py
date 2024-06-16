# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node: TreeNode, maxsofar):
        if not node:
            return 0
        cnt = 0
        if node.val >= maxsofar:
            cnt += 1
            maxsofar = node.val
        left = dfs(node.left, maxsofar)
        right = dfs(node.right, maxsofar)
        return left + right + cnt

#solution function
def goodNodes(root: TreeNode) -> int:
    
    return dfs(root, float('-inf'))