from collections import defaultdict

def countComponents(n: int, edges: list[list[int]]) -> int:
    ###preprocessing
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x) #undirected
    
    #isolated vertices
    for i in range(n):
        if i not in graph:
            graph[i] = []
    
    ###preprocessing end


    def dfs(start: int) -> None:
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in seen: #to prevent redundant searches
                    seen.add(neighbor)   #to prevent redundant searches
                    stack.append(neighbor)
        return
    
    
    count = 0 #number of provinces
    seen = set()
    for node in graph:
        #if statement only runs when a node in a new connected component comes in
        if node not in seen:
            seen.add(node)
            count += 1
            dfs(node)
    return count