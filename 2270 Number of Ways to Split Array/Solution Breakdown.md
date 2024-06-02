## 2270. Number of Ways to Split Array

>Description: [2270. Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/description/)\
You are given a 0-indexed integer array `nums` of length `n`.\
`nums` contains a valid split at index `i` if the following are true:
- The sum of the first `i + 1` elements is greater than or equal to the sum of the last `n - i - 1` elements.
- There is at least one element to the right of `i`. That is, `0 <= i < n - 1`.

Constraints:

- <code>2 <= nums.length <= 10<sup>5</sup></code> 
- <code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code> 

### Solution 1: 

```python

def waysToSplitArray(nums: list[int]) -> int:
    
    #cumulative sum array
    prefixsum = [nums[0]]
    for i in range(1, len(nums)):
        prefixsum.append(nums[i] + prefixsum[-1])
    
    #comparing
    vsplit = 0 #count of valid split
    for j in range(len(prefixsum) - 1):
        if prefixsum[j] >= prefixsum[-1] - prefixsum[j]:
            vsplit += 1
    
    return vsplit
return sublength
```
### Breakdown of Solution:

**Preprocessing: Prefixsum**

What we are interested here is 'cumulative sums.'\
It is inefficient to calculate the cumulative sums while we iterate through the given array using for loop.\
The idea is, if we have to calculate the cumulative sums, why not do it at first? Then, with cumulative sums array we obtained, we can simply extract required elements from that prefixsum array, each of which will cost only O(1).

The cumulatvie sum of the first subarray would simply be `prefixsum[i]` and the sum of latter subarray can also be computed with two elements for prefixsum: `prefixsum[-1]` and `prefixsum[i]`.

One interesting fact is that you do not need to check for the last element of prefixsum; Per description, there has to be at least one element to the right for a valid split. Hence `len(prefixsum) **- 1**`

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of nums to build prefixsum and iteration of prefixsum -> O(2n)

Space Complexity: *O(n)*

- storing prefixsum and constants


### Solution 2: do not even require prefixsum

 ```python

def waysToSplitArray(nums: list[int]) -> int:
    
    left_sum  = 0
    total_sum = sum(nums)

    vsplit = 0
    for i in range(len(nums) - 1):
        left_sum += nums[i]             #cumulative sum on the go
        right_sum = total_sum - left_sum
        
        if left_sum >= right_sum:
            vsplit += 1

    return vsplit
```
### Breakdown of Solution:

**Preprocessing: Prefixsum**

The underlying idea is same, however, here we calculate the cumulative sum on the go. All the rest is same. Space complexity improved.

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of nums twice (one for sum method, the other for for loop) -> O(2n)

Space Complexity: *O(1)*

- storing constants