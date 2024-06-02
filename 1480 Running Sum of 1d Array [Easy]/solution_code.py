def runningSum(nums: list[int]) -> list[int]:
    
    runsum = [nums[0]]
    for i in range(1, len(nums)):
        runsum.append(runsum[-1] + nums[i])
    
    return runsum