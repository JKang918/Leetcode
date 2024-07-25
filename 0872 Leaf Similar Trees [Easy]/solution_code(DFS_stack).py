from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


    #DFS: iterative stack

    def dfsStack(treenode):
        leaf = []    
        stack = [treenode]

        while stack:
            node = stack.pop()

            if not node.left and not node.right:
                leaf.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaf
    
    return dfsStack(root1) == dfsStack(root2)