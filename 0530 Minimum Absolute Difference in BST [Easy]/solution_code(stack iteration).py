from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
        stack = []
        values = []
        curr = root

        # when no "or curr", it only searchs the left subtree from the root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                #inorder beg
                values.append(curr.val)
                #inorder end
                curr = curr.right
        
        return values


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    
    value = list()
    dfs(root, value)
    diff = float('inf')
    for i in range(0, len(value) - 1):
        diff = min(diff, value[i + 1] - value[i])
        if diff == 1: return 1
    return diff