## 1167. Minimum cost to connect sticks

>Description: [1167. Minimum cost to connect sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)\
Check out the link above.


Constraints:

- <code>1 <= sticks.length <= 10<sup>4</sup></code> 
- <code>1 <= sticks[i] <= 10<sup>4</sup></code> 


### Solution: 

```python
from typing import List
import heapq

def connectSticks(sticks: List[int]) -> int:

    ans = []

    heapq.heapify(sticks)

    while len(sticks) > 1:
        ans.append(heapq.heappop(sticks) + heapq.heappop(sticks))
        
        heapq.heappush(sticks, ans[-1])
        
    return sum(ans)
```
### Breakdown of Solution:

**Heap**

This problem involves finding the minimum value frequently, so it is appropriate to use a heap, which is very efficient for finding the minimum value.

### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- heapify costs O(nlong(n))
- inbuilt sum function costs O(n)

Space Complexity: *O(n)*

- `ans` list
    
