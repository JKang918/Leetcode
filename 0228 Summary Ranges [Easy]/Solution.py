from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    
    n = len(nums)

    if n == 0:
        return []

    arr = []

    left = 0
    right = 1

    #until penultimate range
    while right < n:
        if nums[right] == nums[right - 1] + 1:
            #sliding window +1
            right += 1
        else: #nums[right] > nums[right - 1] = 1
            arr.append([nums[left], nums[right - 1]])
            #collapse sliding window
            left = right
            right += 1

    #last range
    arr.append([nums[left], nums[right - 1]])

    ans = []
    for beg, end in arr:
        if beg == end:
            ans.append(str(beg))
        else:
            ans.append(str(beg) + "->" + str(end))
    
    return ans