from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: TreeNode) -> int:
        next_level = deque()
        next_level.append(root)

        while next_level:
            curr_level = next_level
            next_level = deque()
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        ans = 0
        for node in curr_level:
            ans += node.val
        
        return ans