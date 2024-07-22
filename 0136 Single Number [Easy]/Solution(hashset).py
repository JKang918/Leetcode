from typing import List

def singleNumber(nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            seen.remove(num)
    
    for e in seen:
        return e