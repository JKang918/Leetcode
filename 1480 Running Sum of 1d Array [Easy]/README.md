## 1480. Running Sum of 1d Array

>Description: [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/description/)\
Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.\
Return the running sum of `nums`.

Constraints:

- <code>-10<sup>6</sup> <= nums[i] <= 10<sup>6</sup></code> 
- `1 <= nums.length <= 1000`

### Solution: 

```python
def runningSum(nums: list[int]) -> list[int]:
    
    runsum = [nums[0]]
    for i in range(1, len(nums)):
        runsum.append(runsum[-1] + nums[i])
    
    return runsum
```
### Breakdown of Solution:

**Prefixsum**

This problem itself is rather easy but its importance is coming from its applicability in other complex problems.\
As part of preprocessing, sometimes we need to build a prefixsum array, of which elements are the cumulative sums of a given array upto that index.

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of nums

Space Complexity: *O(n)*

- storing `runningsum`
