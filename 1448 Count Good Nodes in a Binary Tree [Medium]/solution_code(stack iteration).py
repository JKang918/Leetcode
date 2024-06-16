# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, maxsofar):
        if not node: return 0
        stack = [(node, maxsofar)]
        cnt = 0
        while stack:
            node, maxsofar= stack.pop()
            if node.val >= maxsofar:
                cnt += 1
                maxsofar = node.val

            if node.right:
                stack.append((node.right, maxsofar))
            if node.left:
                stack.append((node.left, maxsofar))
        return cnt

#solution function
def goodNodes(root: TreeNode) -> int:
    
    return dfs(root, float('-inf'))