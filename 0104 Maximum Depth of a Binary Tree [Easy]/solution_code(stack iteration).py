from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [(root, 0)]
    ans = 0
    while stack:
        node, depth = stack.pop()
        ans = max(depth, ans)
        if node.right:
            stack.append((node.right, depth + 1))

        if node.left:
            stack.append((node.left, depth + 1))
    return ans + 1