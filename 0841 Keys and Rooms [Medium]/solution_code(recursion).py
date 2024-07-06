def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    
    seen = {0}

    #recursive
    def dfs(start):
        room = start
        for neighbor in rooms[room]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    dfs(0)
    return len(seen) == len(rooms)