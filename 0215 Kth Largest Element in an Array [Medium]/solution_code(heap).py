from typing import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:

    
    nums = [- num for num in nums]
    heapq.heapify(nums)

    for _ in range(k - 1):
        heapq.heappop(nums)
    
    return - heapq.heappop(nums)