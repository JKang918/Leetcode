## 2090. K Raidus Subarray Averages

>Description: [2090 K Raidus Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/description/)\
This problem is quite long with lots of examples, so click the description instead to see the description.

Constraints:

- <code>1 <= nums.length <= 10<sup>5</sup></code> 
- <code>0 <= nums[i], k <= 10<sup>5</sup></code> 

### Solution: 

```python
def getAverages(nums: list[int], k: int) -> list[int]:
    
    if k == 0: return nums
    if len(nums) < (2*k + 1): return [-1] * len(nums)

    #result: output array
    #[-1] -> update when k-radius avg exists for index i 
    result = [-1] * len(nums)
    
    #k-radius avg exists starting (2k + 1) elements -> index of k
    #Last k-radius avg -> when k elemnts are left on the right -> index of [len(array) - (k+1)]
    
    """
    First subarray with valid k-radius avg
    [nums[0], ..., nums[k] ,... , nums[2k]] -> total (2k + 1) elements

    Second subarray
    [nums[1], ..., nums[k+1] ,... , nums[2k+1]]
    ...

    Last subarray
    [nums[n-(2k+1)]... , nums[n-(k+1)], ... , nums[n-1]]
    """
    
    #k-radius sum of the first subarray
    radavg = sum(nums[:(2*k + 1)]) #Beware!! nums[:2k] is nums[0] to nums[2k-1] 
    result[k] = radavg//(2*k + 1)

    """
    In the while loop:

    radavg += nums[(2*k + 1)] - nums[0]
    result[k+1] = radavg/(2*k + 1)
    
    Until 2k + 1 hits the last element in nums
    """

    j = 1
    while (2*k + j) < len(nums):
        radavg += nums[(2*k + j)] - nums[(j - 1)]
        result[k + j] = radavg//(2*k + 1)
        j += 1
    
    return result
```
### Breakdown of Solution:

**Sliding Windows and Prefixsum**

To obtain k-radius average, the subarray should be of length of `2k + 1`. This constraint makes the problem fit for sliding window solution. 

Store the k-radius average into the output array's `k`th index. The rests are about installing bound conditions.

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of nums

Space Complexity: *O(n)*

- storing `result` and constants
