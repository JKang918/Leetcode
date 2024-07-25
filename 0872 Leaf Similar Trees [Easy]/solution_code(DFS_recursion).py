from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

    #DFS recursive function
    def dfs(treenode, leaf: List) -> None:

        node = treenode

        if not node:
            return 

        if not node.left and not node.right:
            leaf.append(node.val)

        if node.left:
            dfs(node.left, leaf)

        if node.right:
            dfs(node.right, leaf)
        
        return
    
    leaf1 = []
    leaf2 = []
    dfs(root1, leaf1)
    dfs(root2, leaf2)
    return leaf1 == leaf2