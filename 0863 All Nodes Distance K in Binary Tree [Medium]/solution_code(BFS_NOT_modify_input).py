from collections import deque
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

####################################

def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    
    #idea: 1. graph 2. do bfs(graph) from that node

    ###preprocessing: from tree to graph
    graph = defaultdict(list)
    queue = deque([root])

    while queue:
        curr_level = len(queue)
        for i in range(curr_level):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val) #undirected
            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val) #undirected
####################################

    queue = deque([target.val])
    seen = {target.val}
    #ans = []

    #k distance from target
    for j in range(k):
        curr_level = len(queue)
        for n in range(curr_level):
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
    ###end of the outer for loop: queue with k distance nodes
    
    return [node for node in queue]