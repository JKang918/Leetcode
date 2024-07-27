## 2294. Partition Array Such That the Maximum Difference is K

>Description: [2294. Partition Array Such That the Maximum Difference is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/)\
Check out the link above

Constraints:

- <code>1 <= nums.length <= 10<sup>5</sup></code> 
- <code>0 <= nums[i] <= 10<sup>5</sup></code>
- <code>0 <= k <= 10<sup>5</sup></code> 

### Solution: 

```python
from typing import List

def partitionArray(nums: List[int], k: int) -> int:
    
    nums.sort() 
    count = 1
    x = nums[0]

    for i in range(1, len(nums)):
        if (x + k) < nums[i]:
            count += 1
            x = nums[i]
    
    return count
```
### Breakdown of Solution:

**Greedy Algorithm**

The idea is, cramming as many numbers in an array. 

So while traversing the given array, if a certain element is below the starting element in a substring, `x`, put that all into one substring along with `x`.

When an element finally comes along that goes beyond the limit, `(x, k)`, start a new substring. 

The idea that doing something as much as possible at every step calls for greedy algorithm.

### Complexity Analysis:

Time Complexity: *O(nlong(n))*

- sorting and traversing

Space Complexity: *O(1)*

- constants