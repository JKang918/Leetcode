def getAverages(nums: list[int], k: int) -> list[int]:
    
    if k == 0: return nums
    if len(nums) < (2*k + 1): return [-1] * len(nums)

    #result: output array
    #[-1] -> update when k-radius avg exists for index i 
    result = [-1] * len(nums)
    
    #k-radius avg exists starting (2k + 1) elements -> index of k
    #Last k-radius avg -> when k elemnts are left on the right -> index of [len(array) - (k+1)]

    #k-radius sum of the first subarray
    radavg = sum(nums[:(2*k + 1)]) #Beware!! nums[:2k] is nums[0] to nums[2k-1] 
    result[k] = radavg//(2*k + 1)

    j = 1
    while (2*k + j) < len(nums):
        radavg += nums[(2*k + j)] - nums[(j - 1)]
        result[k + j] = radavg//(2*k + 1)
        j += 1
    
    return result