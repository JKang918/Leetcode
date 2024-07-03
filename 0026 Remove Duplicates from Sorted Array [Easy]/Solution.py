def removeDuplicates(nums: list[int]) -> int:

    ref = nums[0]

    #start with the second element
    i = 1
    while i < len(nums):
        if nums[i] == ref:
            nums.pop(i)
        else:
            ref = nums[i]
            i += 1
    
    return len(nums)