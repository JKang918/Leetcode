## 1710. Maximum Units on a Truck
 
>Description: [1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/description/)\
Check out the link for description

Constraints:

- `1 <= boxTypes.length <= 1000`
- `1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000`
- <code>1 <= truckSize <= 10<sup>5</sup></code> 


### Solution

```python
from typing import List
import heapq


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    
    boxTypes2 = []

    for boxcnt, unit in boxTypes:
        #-unit to simulate max heap
        boxTypes2.append([-unit, boxcnt])
    
    heapq.heapify(boxTypes2)

    totalUnits = 0
    
    #if trucSize == 0 => no left space in truct, skip the loop and return current totalUnits loaded
    #if boxTpyes2 is empty => all loaded but the truck still has some spaces left, skip the loop return current totalUnits loaded
    while truckSize and boxTypes2:
        #unit is negative, boxcnt is positive
        unit, boxcnt = heapq.heappop(boxTypes2)
        
        #still spaces left or perfectly fit
        if (truckSize - boxcnt) >= 0:
            truckSize -= boxcnt #if perfectly fit, would be zero, ending the loop
            #because unit is negative
            totalUnits -= (unit * boxcnt)
        
        #current empty space if not large enough
        else:
            totalUnits -= (unit * truckSize)
            truckSize = 0

    return totalUnits
```

### Breakdown of Solution:

**Greedy Algorithm (Heap)**

To maximize the number of units loaded on a truck, load boxes with the most units in them at every step. So this is a greedy algorithm problem.


#### 1. MAX heap

```python
    boxTypes2 = []

    for boxcnt, unit in boxTypes:
        #-unit to simulate max heap
        boxTypes2.append([-unit, boxcnt])
    
    heapq.heapify(boxTypes2)
```

To return the heaviest (most units) box every time, we need max heap that sorts boxes in accordance with the number of units in each box.

Because heap sorts things in the order of first value in case of list of lists or list of tuples, I swapped the location of two elements in each inner list.

On the other hand, because heapq in python does not provide max heap, I put negative sign in front of `unit` to structure max heap.

### 2. Load boxes, until either 1. boxes are all loaded or 2. truck is full

```python
    totalUnits = 0
    
    #if trucSize == 0 => no left space in truct, skip the loop and return current totalUnits loaded
    #if boxTpyes2 is empty => all loaded but the truck still has some spaces left, skip the loop return current totalUnits loaded
    while truckSize and boxTypes2:
        #unit is negative, boxcnt is positive
        unit, boxcnt = heapq.heappop(boxTypes2)
        
        #still spaces left or perfectly fit
        if (truckSize - boxcnt) >= 0:
            truckSize -= boxcnt #if perfectly fit, would be zero, ending the loop
            #because unit is negative
            totalUnits -= (unit * boxcnt)
        
        #current empty space if not large enough
        else:
            totalUnits -= (unit * truckSize)
            truckSize = 0

    return totalUnits
```

`totalUnits`: output value. The number of boxes loaded on a truck.

`While truckSize and boxTypes2` : loading goes on until truck is full or boxes are all loaded

**Loading process**

1. `truckSize - boxcnt`: check whether there is enough space for boxes. These boxes are heaviest ones in each respective step.
2. If there is enough space to load all of the above boxes
    1) load them all and `truckSize` will be reduced
    2) track total number of boxes loaded. Don't forget `unit` is negative value so you have to subtract them again.
3. if `truckSize` is non zero (capacity o) and boxes are left (`boxTypes2` not empty), continue loading
    1) if not, return `totalUnits`, which is the number of boxes loaded on the truck



### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- heapify

Space Complexity: *O(n)* or `O(1)`

- `boxTypes2` but if you choose to modify the input, no additional space required other than contants