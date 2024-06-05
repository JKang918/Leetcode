## 525. Contiguous Array

>Description: [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/description/)\
Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number* of `0` and `1`.

Constraints:

- <code>1 <= nums.length <= 10<sup>5</sup></code> 
- `nums[i]` is either `0` or `1`

### Solution: 

```python
def findMaxLength(nums: list[int]) -> int:
    
    count = dict()
    count[0] = -1 #!!!
    ans = 0
    prefix = 0
    
    for i in range(len(nums)):
        if nums[i] == 0: prefix -= 1
        else:            prefix += 1
        
        if prefix not in count: count[prefix] = i

        ans = max(ans, i - count[prefix])
    
    return ans
```
### Breakdown of Solution:

**Hash table**

This problem can be better understood with an example:

| index (dict.values) | 0  | 1 | 2  | 3  | 4  | 5  | 6  | 7 | 8  |
|:-------------------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| element             | 0  | 1 | 0  | 0  | 1  | 0  | 1  | 1 | 0  |
| prefix (dict.key)   | -1 | 0 | -1 | -2 | -1 | -2 | -1 | 0 | -1 |


We calculate something similar to prefix sum; the only twist is instead only simply calculating cumulative sum, for `0`s, **add `-1`**.\
This is expressed in the third row.

Note that the marginal cumulative sum is zero when the exactly same number of `-1`s and `1`s are added.\
For example, prefix of index 6 and index 2 are same. Meaning, `[nums[3], ... , nums[6]]` is one the subarrays we are looking for.

In other words, by subtracting the smaller index from the larget index with the same prefix (= `i - count[prefix]`) gives you the length of the subarray.

`count` dictionary is to store this information, prefix for key, index information for values.

One adjusted ment to make is `count[0] = -1`.\
When the prefix of 0 means the length of valid subarray is itself.\

For example, for index 7, the prefix is 0, the length of the valid subarray should be 8, from the 1st element to the 8th element.\
With `i` being 7 and `count[0]` being -1, we can obtaine the length, 8.

The same goes for other indices with the prefix of 0.

Lastly, `ans` is updated only in the case of a longer valid subarray.

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of nums

Space Complexity: *O(n)*

- storing `count`
