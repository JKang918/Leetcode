def maximumSum(nums: list[int]) -> int:
    ans = -1
    soddict = dict()
    # {sum of digits : max of all associated nums[i]s}
    for i in range(len(nums)):
        
        sod = 0
        k = 0
        while nums[i]//(10**k) >= 10:
            sod += (nums[i]//(10**k)) % 10
            k += 1
        sod += (nums[i]//(10**k))

        if sod not in soddict:
            soddict[sod] = nums[i]
        else:
            ans = max(ans, soddict[sod] + nums[i])
            soddict[sod] = max(soddict[sod], nums[i])
    
    return ans