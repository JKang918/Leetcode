## 643. Maximum Average Subarray I

>Description: [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/description/)\
You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than `10<sup>5</sup>` will be accepted..

Constraints:

- `n == nums.length`
- `1 <= k <= n <= 10<sup>5</sup>`
- `-104 <= nums[i] <= 10<sup>4</sup>`

### Solution: 

```python
def findMaxAverage(nums: list[int], k: int) -> float:
    
    ans = curr = left = 0
    
    #make initial value of curr as the firt k sum of nums
    for i in range(k):
        curr += nums[i]
    #ans, curr: sum of elements for the first k-length subarray    
    ans = curr
    
    
    for right in range(k, len(nums)):
        
        # curr: sum of elements for the next k-length subarray
        curr += nums[right]
        curr -= nums[left]
        left += 1

        ans = max(ans, curr)
    
    # the max of all currs
    #ans = float(ans) #not required in python
    ans = ans/k
    return ans
```
### Breakdown of Solution:

**Sliding Windows using Two Pointers**

This problem is easily solved with sliding windows using two pointers: `left` and `right`\
Make sure to understand that the window length is constant throughout the whole iterative process.

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of nums

Space Complexity: *O(1)*

- storing constants only