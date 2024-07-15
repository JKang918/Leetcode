## 2208. Minimum Operations to Halve Array Sum

>Description: [2208. Minimum Operations to Halve Array Sum](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description/)\
Check out the link above for description.

Constraints:

- <code>1 <= nums.length <= 10<sup>5</sup></code> 
- <code>1 <= nums[i] <= 10<sup>7</sup></code>

### Solution: 

```python
from typing import List
import heapq

def halveArray(nums: List[int]) -> int:
    #get the max value and halve that

    #to simulate max heap in heapq
    nums = [-num for num in nums]

    #O(n log(n))
    heapq.heapify(nums)

    sums = sum(nums)
    target = sums / 2

    #because both are negatvies
    count = 0
    while sums < target:
        x = heapq.heappop(nums)
        x = x/2
        heapq.heappush(nums, x)
        sums -= x
        
        count += 1
    
    return count
```
### Breakdown of Solution:

**Heap**

At every iteration we need to get the max value, halve it, and push it back into the heap. This way, the summation of all values decreases the fastest, minimizing the number of iteration (`count`) we need to perform.

Since `heapq` do not provide maxheap separately, to simulate max heap we turn every value in the input list into negative values.


### Complexity Analysis:

Time Complexity: *O(n * log(n))*

- Turning a python list to a heap in heapq takes O(n)
- Heap sorting takes O(log(n))

Space Complexity: *O(1)* or *O(n)*

- In the above solution, I did modify the input to save space. So here it took O(1) space only.
- However, if you declare a separate list to copy the input, on which you perform heap functions, it would be O(n).
