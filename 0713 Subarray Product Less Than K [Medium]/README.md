## 713. Subarray Product Less Than K

>Description: [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/description/)\
Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

Constraints:

- `1 <= nums.length <= 3 * 104`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 106`

### Solution: 

```python
def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    
    #abnormal cases: k = 0, k = 1
    if k <= 1:
        return 0

    ans = left = 0
    product = 1
    
    # Two pointers: left and right to form sliding window
    for right in range(len(nums)):
        
        product *= nums[right]    
        
        #shrink the window if it does not meet the condition
        while product >= k:
            product //= nums[left]
            left += 1
        
        # the number of subarrays in a given window
        ans += (right + 1) - left
    
    return ans
```
### Breakdown of Solution:

**Sliding Windows using Two Pointers**

| index          | 0       | 1       | ... | `left`       | ... | `right`       | ... | n - 1       |
|:--------------:|:-------:|:-------:|:---:|:-------:|:---:|:-------:|:---:|:-------------------:|
| array elements | nums[0] | nums[1] |  ...   | nums[left] |  ...   | nums[right] |  ...   | nums[n - 1] |
| cumulative product     | -      | -      | -  | -      | -  | product of (`left` to `right`) < `k`    | -  | -   

Suppose the product of elements from `left` to `right` is strictly below `k`, then the number of subarrays satisfiying the condition should be `right + 1 - left` (both end inclusive).\
This is why `(right + 1) - left` is added to the output variable. The subarrays are below:

- [right]
- [right - 1, right]
- [right - 2, right - 1, right]
- ...
- [left, left + 1, ... , right - 1, right]

What happens when the product exceeds the limitation?

| index          | 0       | 1       | ... | `left + 1`       | ... | `right`       | ... | n - 1       |
|:--------------:|:-------:|:-------:|:---:|:-------:|:---:|:-------:|:---:|:-------------------:|
| array elements | nums[0] | nums[1] |  ...   | nums[left + 1] |  ...   | nums[right] |  ...   | nums[n - 1] |
| cumulative product     | -      | -      | -  | -      | -  | product of (`left + 1` to `right`) < `k`\ product of (`left` to `right`) >= `k`    | -  | -   

This case, we shrink the window by increasing left by 1 at a time. This is represented above in `the while loop`.\
The maximum value `left` can take is `right + 1`. This occurs when `nums[right]` itself alone exceeds the limit.

1. nums[right] >= k
2. while loop begins
    - while loop begins: `left` = `right - 1`
    - `product` after `//=` operations: `nums[right]`
    - `left` after `+= 1`: `left` = `right`
    - while loop ends
    - while loop begins: `left` = `right`
    - `product` after `//=` operations: `1`
    - `left` after `+= 1`: `left` = `right + 1`
3. while loop ends: `product = 0`, which is smaller than `k`
4. becuase `left` = `right + 1`, none is added to `ans`

This is why not only `k = 0` but also `k = 1` is excluded from the beginning. Because if not excluded, the while loop never ends and the index (`left`) exceeds the list.\
Also, this is aligned with the intuition; if `k = 1`, the product can never go below `1`. (Recall the constraint)

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of nums

Space Complexity: *O(1)*

- storing constants only
    
