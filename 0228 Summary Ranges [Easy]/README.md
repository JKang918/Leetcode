## 228. Summary Ranges

>Description: [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/description/)\
Check out the link above.

Constraints:

- `0 <= nums.length <= 20`
- <code>-2<sup>31</sup> <= nums[i]  <= 2<sup>31</sup>-1</code> 
- All the values of `nums` are **unique**.
- nums is sorted in **ascending order**.

### Solution: 

```python
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
```
### Breakdown of Solution:

**Two Pointers - Sliding Window**

We use two pointers, `left` and `right` to implementl the method of sliding window.

`right` pointer starts with the second value and goes on till it hits the end of the values in the array.
At every iteration, check whether the incremental range breaks up. If it does so, start the new range by collapsing the sliding window and store the previous range in an empty list.

Note that the last range should be appended separately at the end of the while loop.

The next part in the code is simply turing stored ranges into the required string format.

### Complexity Analysis:

Time Complexity: *O(n)*

- sliding window

Space Complexity: *O(n)*

- lists
