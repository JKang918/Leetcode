## 2126. Destroying Asteroids

>Description: [2126. Destroying Asteroids](https://leetcode.com/problems/destroying-asteroids/)\
Check out the link above for description.

Constraints:

- <code>1 <= mass <= 10<sup>5</sup></code> 
- <code>1 <= asteroids.length <= 10<sup>5</sup></code>
- <code>1 <= asteroids.[i] <= 10<sup>5</sup></code>

### Solution: 

```python
from typing import List
import heapq

def asteroidsDestroyed(mass: int, asteroids: List[int]) -> bool:
    #best case scenario: planet hit by min asteroid each time to gain mass, not being destroyed
    
    heapq.heapify(asteroids)

    while asteroids:
        if mass >= asteroids[0]:
            mass += heapq.heappop(asteroids)
        else:
            return False
    
    return True
```
### Breakdown of Solution:

**Heap (Greedy Algorithm)**

The best case scenario for the planet to withstand all the asteroids is where the planet hit by min mass asteroid at each round and gain mass from it.

To extract min mass asteroid effectively, use heap structure.

Whenever the planet can withstand the min mass asteroid, increment the planet's mass by the mass of min mass asteroid. When it cannot, return False.

### Complexity Analysis:

Time Complexity: *O(n * log(n))*

- Turning a python list to a heap in heapq takes O(n)
- Heap sorting takes O(log(n))

Space Complexity: *O(1)* or *O(n)*

- In the above solution, I did modify the input to save space. So here it took O(1) space only.
- However, if you declare a separate list to copy the input, on which you perform heap functions, it would be O(n).
