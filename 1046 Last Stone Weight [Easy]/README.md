## 1046. Last Stone Weight

>Description: [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/description/)\
Check out the link above for description.

Constraints:

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`


### Solution: 

```python
from typing import List
import heapq

def lastStoneWeight(stones: List[int]) -> int:

    #turn it into negative weights to simulate max heap
    stones = [-stone for stone in stones]    

    heapq.heapify(stones)

    #until there is one last remaining stone
    while len(stones) > 1:
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)
        heapq.heappush(stones, stone1 - stone2)

    #to turn in back to a positive integer 
    return -stones[0]
```
### Breakdown of Solution:

**Heap**

At every iteration we need to get two max values. This befits the data structure, heap as it takes only O(1) to get max values from heap.

Since `heapq` do not provide maxheap separately, to simulate max heap we turn every value in the input list into negative values.

Until we are left with only one value in `stones`, we take two largest values, get the difference, push it back to the heap.

### Complexity Analysis:

Time Complexity: *O(n * log(n))*

- Turning a python list to a heap in heapq takes O(n)
- Heap sorting takes O(log(n))

Space Complexity: *O(1)* or *O(n)*

- In the above solution, I did modify the input to save space. So here it took O(1) space only.
- However, if you declare a separate list to copy the input, on which you perform heap functions, it would be O(n).
