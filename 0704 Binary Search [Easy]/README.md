## 704. Binary Search

>Description: [704. Binary Search](https://leetcode.com/problems/binary-search/)\
Check out the link above

Constraints:

- <code>1 <= nums.length <= 10<sup>4<sup\><code\>
- <code>-10<sup>4<sup\> <= nums.[i], target <= 10<sup>4<sup\><code\>
- `0 <= k <= 106`

### Solution: 

```python
from typing import List

def search(nums: List[int], target: int) -> int:
    
    n = len(nums)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid + 1
        
        else: # target < nums[mid]
            right = mid - 1
    
    return -1
```
### Breakdown of Solution:

**Binary Search**

This problem requires an O(log(n)) solution, so we will get an answer using binary search.

Splits the input array, which is sorted in ascending order, in half and look for `target`.

If target value is smaller (or greater) than the mid point value, now search the left (or right) half of the array.

Repeat the above process. If there is no target value, eventually left becomes larger than right or right becomes smaller than left.

In this case, return `-1`.



### Complexity Analysis:

Time Complexity: *O(log(n))*

- binary search

Space Complexity: *O(1)*

- storing constants only
    
