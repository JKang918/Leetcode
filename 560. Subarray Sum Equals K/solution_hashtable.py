def subarraySum(nums: list[int], k: int) -> int:
    
    #count dictionary
    #{cumulative sum : count}
    count = dict()
    count[0] = 1
    curr = 0 
    ans = 0
    for num in nums:
        curr += num
        ans += count.get(curr - k, 0)
        count[curr] = count.get(curr, 0) + 1 
    
    return ans