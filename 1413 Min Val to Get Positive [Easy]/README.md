## 1413. Min Value to Get Positive Step by Step Sum [Easy]

>Description: [1413. Min Value to Get Positive Step by Step Sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/)\
Given an array of integers `nums`, you start with an initial positive value *startValue*.\
In each iteration, you calculate the step by step sum of startValue plus elements in `nums` (from left to right).
Return the minimum positive value of *startValue* such that the step by step sum is never less than 1.


Constraints:

- <code>-10<sup>2</sup> <= nums[i] <= 10<sup>2</sup></code> 
- `1 <= nums.length <= 100`

### Solution: 

```python
def minStartValue(nums: list[int]) -> int:
    
    startValue = 0 #output int
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    if min(prefix) < 0:
        startValue = (-1) * min(prefix) + 1
    else:
        startValue = 1
    
    return startValue
```
### Breakdown of Solution:

**Prefixsum**

The minimum *startvalue* is one. This condition is met by the `else` block.

Otherwise, this is mere another version of obtaining prefix sum array. Refer to [1480 Running Sum of 1d Array](https://github.com/JKang918/Leetcode/blob/main/1480%20Running%20Sum%20of%201d%20Array%20%5BEasy%5D/Solution%20Breakdown.md) for more information.

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of nums and prefix-min method -> O(2n)

Space Complexity: *O(n)*

- storing `prefix` and constancts
