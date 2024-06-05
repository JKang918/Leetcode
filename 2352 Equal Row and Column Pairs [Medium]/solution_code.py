def equalPairs(grid: list[list[int]]) -> int:
    
    rowcount = dict()

    for i in range(len(grid)):
        rowcount[tuple(grid[i])] = rowcount.get(tuple(grid[i]), 0) + 1  
    
    ans = 0
    for j in range(len(grid)):
        col = []
        for k in range(len(grid)):
            col.append(grid[k][j])
        
        ans += rowcount.get(tuple(col), 0)

    return ans