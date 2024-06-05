def twoSum(nums: list[int], target: int) -> list[int]:
    htable = dict()
    
    for i in range(len(nums)):
        if (target - nums[i]) in htable:
            return [htable[target - nums[i]], i]
        htable[nums[i]] = i
    return []