from collections import defaultdict
def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    
    #number of connected component is 1 -> True

    ###preprocessing
    graph = defaultdict(list)
    #for isolated vertices
    for i in range(n):
        graph[i] = []
    #

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x) #undirected
    ###preprocessing end
    
    #DFS: iterative stack
        def dfs(start: int) -> None:
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            return
    
    seen = {source}
    dfs(source)

    return destination in seen