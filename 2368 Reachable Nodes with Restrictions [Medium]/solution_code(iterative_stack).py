from collections import defaultdict


def reachableNodes(n: int, edges: list[list[int]], restricted: list[int]) -> int:
    
    ###preprocesscing
    graph = defaultdict(list)
    
    for i in range(n):
        graph[i] = []
    
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    restricted = set(restricted)
    ###preprocessing end



    #DFS: stack
    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return
    
    seen = {0}
    dfs(0)

    return len(seen)