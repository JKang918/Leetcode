def longestOnes(nums: list[int], k: int) -> int:
    
    zerocount = 0 
    sublength = 0
    left      = 0

    for right in range(len(nums)):
        
        if nums[right] == 0:
            zerocount += 1

        while zerocount > k:
            if nums[left] == 0:
                zerocount -= 1
            left += 1
        
        sublength = max(right + 1 - left, sublength)
    
    return sublength
