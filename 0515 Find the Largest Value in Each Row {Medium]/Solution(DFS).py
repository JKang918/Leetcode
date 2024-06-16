#To use Deque (data structure)
from collections import deque  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root: TreeNode) -> list[int]:
    ans = []
    #DFS function define
    def dfs(node, depth): 
        if not node:
            return []
        
        if len(ans) == depth:
            ans.append(node.val)
        else:
            ans[depth] = max(ans[depth], node.val)
        
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
        return ans
    
    return dfs(root, 0)