## 536. Subarray Sum Equals k 

>Description: [536. Subarray Sum Equals k ](https://leetcode.com/problems/subarray-sum-equals-k/description/)\
Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.


### Solution: 

```python
def subarraySum(nums: list[int], k: int) -> int:

    count = dict()
    count[0] = 1
    curr = 0 
    ans = 0
    for num in nums:
        curr += num
        ans += count.get(curr - k, 0)
        count[curr] = count.get(curr, 0) + 1 
    
    return ans
```
### Breakdown of Solution:

**curr**: prefix sum (cumulative sum) of elements in a given array, nums\
**count**: dictionary with keys of prefix sum and values of the count of the very prefix sum\
**ans**: output to return, number of subarrays satisfiying the condition

***ith iteration***

| index          | 0       | 1       | ... | `j`       | j + 1     | ... | `i`       | ... | n - 1       |
|:--------------:|:-------:|:-------:|:---:|:-------:|:---------:|:---:|:-------:|:---:|:-------------------:|
| array elements | nums[0] | nums[1] |     | nums[j] | nums[j+1] |     | nums[i] |     | nums[n - 1] |
| prefix sum     | ..      | ..      | ..  | `curr - k`       | ..        | ..  | `curr`    | ..  | sum(nums)   

\
At ith iteration, if there is j such that prefix sum at j is 'curr - k', the subarray from 'j+1' to 'i' (inclusive of both ends) is the subarray that satisfies the condition. Since all the possible 'j's has been counted in the previous iterations, we can call the total count of 'j's using .get method. The total count of possible 'j's is the number of subarrays satisfying the condition at ith iteration.

One thing to take note of is the initialization of 'count' dictionalry: 
  count[0] = 1
This can be easily understood thinking of situtation when the prefix, 'curr' itself is 'k'. Then there is only subarray at ith iteration that meets the condition, nums[0:i] so the ans should be added by 1. This is possible only when the dictionary is initialized as above. Because 'curr - k' is zero and count.get(curr- k, 0) should be 1. 

### Complexity Analysis:

Time Complexity: *O(n)*

- one for loop
- *O(1)* for searching the hash table

Space Complexity: *O(n)*

- store hash table with the size of n
    
