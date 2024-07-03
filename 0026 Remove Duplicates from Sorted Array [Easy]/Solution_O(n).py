def removeDuplicates(nums: list[int]) -> int:

    #Two Pointers
    
    i = 1
    for j in range(1, len(nums)):
        if nums[j - 1] != nums[j]:
            nums[i] = nums[j]
            i += 1
    
    return i