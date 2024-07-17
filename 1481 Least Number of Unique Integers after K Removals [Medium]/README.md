## 1481. Least Number of Unique Integers after K Removals

>Description: [1481. Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/)\
Check out the link above.


Constraints:

- <code>1 <= arr.length <= 10<sup>5</sup></code> 
- <code>1 <= arr[i] <= 10<sup>9</sup></code>
- `0 <= k <= arr.length`

### Solution: 

```python
from typing import List
import heapq
    
def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    
    countmap = dict()
    #key: element in arr
    #values: their counts
    for i in range(len(arr)):
        if arr[i] not in countmap:
            countmap[arr[i]] = 1
        else:
            countmap[arr[i]] += 1

    counts = []
    for cnt in countmap.values():
        counts.append(cnt)

    heapq.heapify(counts)
    
    for _ in range(k):
        if counts[0] > 1:
            counts[0] -= 1
        else: #counts[0] == 1
            heapq.heappop(counts)
    
    return len(counts)
```
### Breakdown of Solution:

**Greedy Algorithm**

We search for least frequent element at every step.

#### 1. count map

```python
    countmap = dict()
    #key: element in arr
    #values: their counts
    for i in range(len(arr)):
        if arr[i] not in countmap:
            countmap[arr[i]] = 1
        else:
            countmap[arr[i]] += 1

    counts = []
    for cnt in countmap.values():
        counts.append(cnt)
```
First, record the frequency of each element in the input array in a hash map. This code is not limited to this solution but quite commonly used in other problems.

#### 2. heap

```python
    counts = []
    for cnt in countmap.values():
        counts.append(cnt)

    heapq.heapify(counts)
    
    for _ in range(k):
        if counts[0] > 1:
            counts[0] -= 1
        else: #counts[0] == 1
            heapq.heappop(counts)
    
    return len(counts)
```

Declare an empty array, `counts`.\
Store dictionary values, frequencies, in the array.\

Heapify `counts` to make sure counts[0] is always the least frequent elements frequency, with real-time adjustments.

When the frequency hits zero, pop it away as zero frequency means none of that element is left in the array.

Finally, count the number of distinct elements left in the array using inbuilt `len()` function. 




### Complexity Analysis:

Time Complexity: *O(n)*

- mapping
- removal

Space Complexity: *O(n)*

- map and heap
