def findMaxAverage(nums: list[int], k: int) -> float:
    
    ans = curr = left = 0
    
    for i in range(k):
        curr += nums[i]
    ans = curr
    
    for right in range(k, len(nums)):
        curr += nums[right]
        curr -= nums[left]
        left += 1
        ans = max(ans, curr)
    
    ans = ans/k
    return ans