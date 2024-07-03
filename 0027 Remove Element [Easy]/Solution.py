def removeElement(nums: list[int], val: int) -> int:    
    
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        # nums[j] = val:
            # i stays still, j traverses -> sliding window
