## 1004. Max Consecutive Ones III

>Description: [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/description/)\
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most k `0`'s.

Constraints:

- <code>1 <= nums.length <= 10<sup>5</sup></code> 
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

### Solution: 

```python
def longestOnes(self, nums: list[int], k: int) -> int:
    
    zerocount = 0 #to count the number of 0s in the subarray
    sublength = 0 #output value: length of the valid, logest subarray
    left      = 0 #left pointer

    for right in range(len(nums)):
        
        if nums[right] == 0:
            zerocount += 1

        #zerocount of k or below is tolerated -> no while loop activated
        #zerocount hits k -> while loop activated to compute valid array by shrinking sliding window
        while zerocount > k:
            if nums[left] == 0:
                zerocount -= 1
            left += 1
        
        #length of valid array is updated when its len is greater than the previous ones
        sublength = max(right + 1 - left, sublength)
    
    #max len of valid array returned
    return sublength
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
