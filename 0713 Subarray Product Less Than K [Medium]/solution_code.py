def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    
    if k <= 1:
        return 0

    ans = left = 0
    product = 1
    
    for right in range(len(nums)):
        
        product *= nums[right]    
        
        while product >= k:
            product //= nums[left]
            left += 1
        
        ans += (right + 1) - left
    
    return ans