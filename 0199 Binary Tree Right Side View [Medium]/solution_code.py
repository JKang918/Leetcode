from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode) -> list[int]:
    if not root: return []
    queue = deque([root])
    ans = list()
    while queue:
        lvllen = len(queue)
        for i in range(lvllen):
            node = queue.popleft()
            if i == (lvllen - 1):
                ans.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans