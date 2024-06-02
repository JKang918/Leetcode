#Solution 1
def waysToSplitArray(nums: list[int]) -> int:
    
    #cumulative sum array
    prefixsum = [nums[0]]
    for i in range(1, len(nums)):
        prefixsum.append(nums[i] + prefixsum[-1])
    
    #comparing
    vsplit = 0 #count of valid split
    for j in range(len(prefixsum) - 1):
        if prefixsum[j] >= prefixsum[-1] - prefixsum[j]:
            vsplit += 1
    
    return vsplit

#Solution 2 (superior)
def waysToSplitArray(nums: list[int]) -> int:
    
    left_sum  = 0
    total_sum = sum(nums)

    vsplit = 0
    for i in range(len(nums) - 1):
        left_sum += nums[i]             #cumulative sum on the go
        right_sum = total_sum - left_sum
        
        if left_sum >= right_sum:
            vsplit += 1

    return vsplit
