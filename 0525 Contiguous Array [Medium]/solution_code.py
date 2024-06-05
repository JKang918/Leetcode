def findMaxLength(nums: list[int]) -> int:
    
    count = dict()
    count[0] = -1 #!!!
    ans = 0
    prefix = 0
    
    for i in range(len(nums)):
        if nums[i] == 0: prefix -= 1
        else:            prefix += 1
        
        if prefix not in count: count[prefix] = i

        ans = max(ans, i - count[prefix])
    
    return ans