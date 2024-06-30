from collections import defaultdict

def findCircleNum(isConnected: list[list[int]]) -> int:
    ###preprocessing
    graph = defaultdict(list)

    ##becuase of isolated vertices
    for i in range(len(isConnected)):
        graph[i] = []

    for i in range(len(isConnected) - 1):
        for j in range(i+1, len(isConnected[0])):
            if isConnected[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i) #undirected
    ###preprocessing end
    
    def dfs(start: int) -> None:
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
    
    seen = set()
    count = 0
    for vtx in graph:
        if vtx not in seen:
            seen.add(vtx)
            dfs(vtx)
            count += 1
    return count