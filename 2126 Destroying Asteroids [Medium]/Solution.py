from typing import List
import heapq

def asteroidsDestroyed(mass: int, asteroids: List[int]) -> bool:
    #best case scenario: planet hit by min asteroid each time to gain mass, not being destroyed
    
    heapq.heapify(asteroids)

    while asteroids:
        if mass >= asteroids[0]:
            mass += heapq.heappop(asteroids)
        else:
            return False
    
    return True