def findSmallestSetOfVertices(n: int, edges: list[list[int]]) -> list[int]:
    
    #find all vertices with indegree of zero
    indegree = [0] * n
    
    for x, y in edges:
        indegree[y] += 1
    
    return [node for node in range(n) if indegree[node] == 0]