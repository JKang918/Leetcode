from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:   
    curr_depth = deepest_depth = 0
    deepest_sum = 0
    stack = [(root, 0)]

    while stack:

        node, curr_depth = stack.pop()

        if not node.right and not node.left: #Leaf node
            #if leaf node's depth(curr_depth) is the newest record
            if deepest_depth < curr_depth:
                deepest_depth = curr_depth #update deepest_depth
                deepest_sum = node.val #start adding values
            
            #if leaf node's depth(curr_depth) reaches the deepest_depth so far
            elif deepest_depth == curr_depth:
                deepest_sum += node.val #add the value to the preexisting sum
            
        else:
            if node.right:
                stack.append((node.right, curr_depth + 1))
            if node.left:
                stack.append((node.left, curr_depth + 1))
    
    return deepest_sum