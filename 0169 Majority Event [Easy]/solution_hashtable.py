def majorityElement(nums: list[int]) -> int:
    
    n = len(nums)
    num_count = dict()

    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    for num, count in num_count.items():
        if count > (n/2):
            return num