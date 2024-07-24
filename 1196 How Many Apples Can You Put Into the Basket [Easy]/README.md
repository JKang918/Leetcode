## 1196. How Many Apples Can You Put Into the Basket

>Description: [1196. How Many Apples Can You Put Into the Basket](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description/)\
Check out the link above.

Constraints:

- <code>1 <= weight.length <= 10<sup>3</sup></code>
- <code>1 <= weight[i] <= 10<sup>4</sup></code>


### Solution: 

```python
from typing import List
import heapq

def maxNumberOfApples(self, weight: List[int]) -> int:
    
    heapq.heapify(weight)
    unit = 0
    limit = 5000

    while weight and limit:
        if weight[0] <= limit:
            limit -= heapq.heappop(weight)
            unit += 1
            continue
        else:
            break
    
    return unit
```
### Breakdown of Solution:

**Greedy algorithm**

To maximize the unit, you should put k-lightest elements in the basket.

To get the current lightest one every you check, use data structure, heap.

Whenever there is a left space in the basket (`if weight[0] <= limit:`), put it in the basket.

Elsewise, stop putting apples in basket (`else: break`).

Return how many apples (`unit`) you put in the basket.

### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- `heapify`

Space Complexity: *O(1)*

- constants
