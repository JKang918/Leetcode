from typing import List

def partitionArray(nums: List[int], k: int) -> int:
    
    nums.sort()
    count = 1
    x = nums[0]

    for i in range(1, len(nums)):
        if (x + k) < nums[i]:
            count += 1
            x = nums[i]
    
    return count