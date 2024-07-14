from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

####################################

def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    
    def dfs(node, parent):
        if not node:
            return
        node.parent = parent
        
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)
    
    ###

    distance = 0
    queue = deque([target])
    seen = {target}

    while queue and distance < k:
        curr_level = len(queue)
        for i in range(curr_level):
            node = queue.popleft()
            for neighbor in [node.left, node.right, node.parent]:
                if neighbor not in seen and neighbor:
                    seen.add(neighbor)
                    queue.append(neighbor)
        distance += 1
                
    #print(queue)
    return [node.val for node in queue]    