from typing import List
import heapq

def lastStoneWeight(stones: List[int]) -> int:

    #turn it into negative weights to simulate max heap
    stones = [-stone for stone in stones]    

    heapq.heapify(stones)

    #until there is one last remaining stone
    while len(stones) > 1:
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)
        heapq.heappush(stones, stone1 - stone2)

    #to turn in back to a positive integer 
    return -stones[0]