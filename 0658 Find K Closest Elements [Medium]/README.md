## 658. Find K Closest Elements

>Description: [658. Find K Closest Elements](https://leetcode.com/problems/maximum-average-subarray-i/description/)\
Check out the link above.

Constraints:

- `1 <= k <= arr.length`
- <code>1 <= arr.length <= n <= 10<sup>4</sup></code>
- <code>-10<sup>4</sup> <= arr[i], x <= 10<sup>4</sup></code>
- `arr` is sorted in ascending order.

### Solution: 

```python
from typing import List
import heapq

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    
    distance = dict()

    for i in range(len(arr)):
        #{element's index in array : distance from the very element from x}
        distance[i] = abs(arr[i] - x)
    
    #heap
    dist = []

    for key, value in distance.items():
        #dist[(distance, index)]
        dist.append((value, key))
    
    #min heap for distance
    heapq.heapify(dist)

    #output(answer) array
    ans = []

    #pop the heap for k times
    for _ in range(k):
        #heappop(dist): (distance, index in arr)
        #heappop(dist)[1]: index
        #arr[index]: k-distance element 
        ans.append(arr[heapq.heappop(dist)[1]])

    #in ascending order
    return sorted(ans)
```
### Breakdown of Solution:

**Heap**

The nature of finding minimum of something makes heap very useful in this problem.

#### 1. start with realizing distance is absolute value of difference.

```python
distance = dict()

    for i in range(len(arr)):
        #{element's index in array : distance from the very element from x}
        distance[i] = abs(arr[i] - x)
```

#### 2. Find the k closest elemenets

```python

    #heap
    dist = []

    for key, value in distance.items():
        #dist[(distance, index)]
        dist.append((value, key))
    
    #min heap for distance
    heapq.heapify(dist)

```

Now we have each the index of element in the input array and its distance from x.\
To find minimum k distances effectively, save this information pairs in a separate array and turn it into a heap.


#### 3. heap pop, k times

```python
        #output(answer) array
        ans = []

        #pop the heap for k times
        for _ in range(k):
            #heappop(dist): (distance, index in arr)
            #heappop(dist)[1]: index
            #arr[index]: k-distance element 
            ans.append(arr[heappop(dist)[1]])

    #in ascending order
    return sorted(ans)
```

Last step is simple: pop the heap k times.

Every time you pop the heap, it will pop a tuple of (its distance from k, index of an element)

We are interested in their actual values, so use their index to random search in the original input array and store k elements in a newly decalred answer array.

Lastly, as the values need to be sorted in an ascending order, use function, `sorted()`.

### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- traverse `arr` (array): O(n)
- traverse `distance` (dictionary): O(n)
- heapify `dist`: O(nlog(n))
- heappop `dist`: O(1)
- sort `ans`: O(log(n))

Space Complexity: *O(n)*

- `distance` and `dist`
