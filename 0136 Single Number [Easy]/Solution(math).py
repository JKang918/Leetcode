from typing import List

def singleNumber(self, nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
    
    return (2*sum(seen)) - sum(nums)