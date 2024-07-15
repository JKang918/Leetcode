from typing import List
import heapq

def halveArray(nums: List[int]) -> int:
    #get the max value and halve that

    #to simulate max heap in heapq
    nums = [-num for num in nums]

    #O(n log(n))
    heapq.heapify(nums)

    sums = sum(nums)
    target = sums / 2

    #because both are negatvies
    count = 0
    while sums < target:
        x = heapq.heappop(nums)
        x = x/2
        heapq.heappush(nums, x)
        sums -= x
        
        count += 1
    
    return count