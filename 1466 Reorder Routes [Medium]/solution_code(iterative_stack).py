from collections import defaultdict

def minReorder(self, n: int, connections: list[list[int]]) -> int:
    ###preprocessing (assume undirected)
    graph = defaultdict(list)

    #no isolated virtex

    route = set()

    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x) #undirected 
        route.add((x, y))  #to check edges #original direction information only

    ###preprocessing end
    
    
    #dfs: traverse away from "0"
        def dfs(node: int):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    ### check whether the original direction is going away from "0"
                    if (node, neighbor) in route: 
                        ans += 1
                    ###
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans
        
    seen = {0}
    
    return dfs(0)