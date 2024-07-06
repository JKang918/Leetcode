def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    
    seen = {0}

    #iterative stack
    stack = [0]

    while stack:
        room = stack.pop()
        for neighbor in rooms[room]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
                
    return len(seen) == len(rooms)