def sortedSquares(nums: list[int]) -> list[int]:

    result = [0] * len(nums)
    
    left  = 0
    right = len(nums) - 1
    for i in range(len(result)):
        if abs(nums[left]) > abs(nums[right]):
            result[len(result) - (i + 1)] = nums[left] ** 2
            left += 1
        else:
            result[len(result) - (i + 1)] = nums[right] ** 2
            right -= 1
    
    return result