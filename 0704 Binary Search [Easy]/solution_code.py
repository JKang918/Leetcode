from typing import List

def search(nums: List[int], target: int) -> int:
    
    n = len(nums)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid + 1
        
        else: # target < nums[mid]
            right = mid - 1
    
    return -1