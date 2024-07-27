## 703. Kth Largest Element in a Stream

>Description: [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)\
Check out the link above.

Constraints:

- <code>1 <= k <= 10<sup>4</sup></code>
- <code>1 <= nums.length <= 10<sup>4</sup></code>
- <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
- <code>-10<sup>4</sup> <= val <= 10<sup>4</sup></code>
- At most <code>10<sup>4</sup></code> calls will be made to `add`.
- It is guaranteed that there will be at least `k` elements in the array when you search for the <code>k<sup>th</sup></code> element.

### Solution: 

```python
from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        
        #leave only k elements in nums
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```
### Breakdown of Solution:

**Heap**

First thing you should realize is that all the elements in `self.nums` that are smaller than K-th largest element are actually irrelevant.

So make `self.nums` a heap and until its length is smaller than or equal to `k`, discard all the other elements.

Whenever a new element is added, run the same command (`while` loop) used in initialization to always maintain the length of the array `k` at maximum.

Return smallest element in the array for `add` function. Because all the elements smaller than k-th largest are gone out of the array already, this one is the k-th largest element.


### Complexity Analysis:

1. Time Complexity (initialization): *O(nlog(n))*

    - heapify: O(n)
    - while: (n - k)
    - heappop: log(n)
    - total: O((n - k)log(n))

2. Time Complexity (add): *O(log(k))*
    - heappop: log(k) 


Space Complexity: *O(k)*

- size of the heap
