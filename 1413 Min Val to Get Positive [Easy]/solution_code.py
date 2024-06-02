def minStartValue(nums: list[int]) -> int:
    
    startValue = 0 #output int
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    if min(prefix) < 0:
        startValue = (-1) * min(prefix) + 1
    else:
        startValue = 1
    
    return startValue