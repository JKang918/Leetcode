## 881. Boats to Save People

>Description: [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/description/)\
Check out the link above.

Constraints:

- <code>1 <= people.length <= 5 * 10<sup>4</sup></code>
- <code>1 <= people[i] <= limit <= 3 * 10<sup>4</sup></code>


### Solution: 

```python
from typing import List

def numRescueBoats(people: List[int], limit: int) -> int:

    people.sort()
    boats = 0
    left = 0
    right = len(people) - 1

    while left <= right:
        if (people[left] + people[right]) <= limit:
            
            left += 1
            
        right -= 1
        boats += 1

    return boats
```
### Breakdown of Solution:

**Greedy algorithm**

A separate boat is required for the heaviest person.

The way to minimize the boat number is to squeeze two people whenever possible into a boat. When it comes to the heaviest person, he needs a separate boat if the lightest person cannot get fit into the same boat.

Sort the array, `people`, in ascending order first. Then assign a new boat for the heaviest person at each step. Check whether the lightest person can be fit into the same boat. 

### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- sorting and traversing

Space Complexity: *O(1)*

- constants
