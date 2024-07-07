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


    #DFS: recursive
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen and neighbor not in restricted:
                seen.add(neighbor)
                dfs(neighbor)
        return

    seen = {0}
    dfs(0)

    return len(seen)