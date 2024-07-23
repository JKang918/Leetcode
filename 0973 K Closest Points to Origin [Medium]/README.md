## 973. K Closest Points to Origin

>Description: [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)\
Check out the link above

Constraints:

- <code>1 <= k <= points.length <= 10<sup>4</sup></code> 
- <code>-10<sup>4</sup> <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>4</sup></code> 

### Solution 1. Heap: 

```python
from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:

    n = len(points)
    distance = {i : points[i][0] ** 2 + points[i][1] ** 2 for i in range(n)}

    heap = []
    for pointIndex, dist in distance.items():
        heap.append((dist, pointIndex))
    heapq.heapify(heap)

    ans = []
    for _ in range(k):
        dist, pointIndex = heapq.heappop(heap)
        ans.append(points[pointIndex])
    
    return ans
```

### Breakdown of Solution:

**Heap**

First, create a dictionary to store distance information for each point in the `points`. To be precise, it is a distance squared.

Second, traverse the dictionary: return distance(value) and index in `points`(key) into a list of tuples.

Third, convert the python list to python heapq heap. Then, every time we heappop the heap, the smallest value (smallest distance) will pop up.

Fourh, pop the heap `k` times. Return the popped distinct integers. 

### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- heapify, traversals

Space Complexity: *O(n)* 

- `heap`, `ans`, `freq`

---

### Solution 2. Quickselect: 

```python
from typing import List
import random

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:

    #dictionary: pointIndex - distance of points[pointIndex] from origin
    n = len(points)
    distance = {i: points[i][0]**2 + points[i][1]**2 for i in range(n)}
    
    #input values are pointIndex
    def partition(left: int, right: int, pivot_pointIndex: int) -> int:

        #pivot point's distance from origin
        pivot_dist = distance[pivot_pointIndex]

        #push pivot point to the end of the given section (left, right) of points
        #do not forget to change the dictionary of distances accordingly
        points[pivot_pointIndex], points[right] = points[right], points[pivot_pointIndex]
        distance[pivot_pointIndex], distance[right] = distance[right], distance[pivot_pointIndex]

        #sorting
        store_pointIndex = left
        for i in range(left, right):
            #if a points[i]'s distance from origin is smaller than that of pivot
            if distance[i] < pivot_dist:
                #swap points[i] with points[store_pointIndex
                #do not forget to change the dictionary of distances accordingly
                points[i], points[store_pointIndex] = points[store_pointIndex], points[i]
                distance[i], distance[store_pointIndex] = distance[store_pointIndex], distance[i]
                store_pointIndex += 1
        #end of for loop
        #all points with smaller distances will be located in points[0] ... points[store_pointIndex - 1]
        #pivot will be at points[right]

        #swap points[right] (= pivot) with points[store_pointIndex]
        #pivot will be points[sotre_pointIndex] with all smaller distance points to the left of itself
        points[right], points[store_pointIndex] = points[store_pointIndex], points[right]
        distance[right], distance[store_pointIndex] = distance[store_pointIndex], distance[right]

        #return the pointIndex of pivot 
        return store_pointIndex

    def quickselect(left: int, right: int, k_closest: int) -> None:

        #no sorting required
        if left == right:
            return

        #otherwise
        #pick random pivot point
        pivot_pointIndex = random.randint(left, right)

        #sorting in order of distance from origin
        pivot_pointIndex = partition(left, right, pivot_pointIndex)

        #if pivot is at the target index
        if pivot_pointIndex == k_closest:
            return

        #otherwise
        #if pivot comes after the target index
        #do sorting again in the section that comes before pivot_pointIndex
        elif k_closest < pivot_pointIndex:
            quickselect(left, pivot_pointIndex - 1, k_closest)

        #otherwise
        #if pivot comes before the target index
        #do sorting again in the section that comes after pivot_pointIndex
        else:
            quickselect(pivot_pointIndex + 1, right, k_closest)
        
        return

    #0-index: points[k - 1] would be the k - closest point
    quickselect(0, n - 1, k - 1)

    #points[ : k] = points[0], points[1], ... , points[k -1] -> k-closest points
    return points[ : k]
```
### Breakdown of Solution:

**Quickselect Algorithm**

The [leetcode editorial](https://leetcode.com/problems/k-closest-points-to-origin/editorial/) provides excellent explanation as to the underlying mechanism of quickselect algorithm.

Here I explain mainly how each line works in the code implementation.


#### Part 1.

```python
    #dictionary: pointIndex - distance of points[pointIndex] from origin
    n = len(points)
    distance = {i: points[i][0]**2 + points[i][1]**2 for i in range(n)}
```

- Construct dictionary, `distance`, to store information about the distance from orgin of each point (`points[i]`)  in `points`.
- Becasue points in `points` are lists and lists are unhashable, take their indices in `points` as keys. 

#### Part 2.

```python
    def quickselect(left: int, right: int, k_closest: int) -> None:

        #no sorting required
        if left == right:
            return

        #otherwise
        #pick random pivot point
        pivot_pointIndex = random.randint(left, right)

        #sorting in order of distance from origin
        pivot_pointIndex = partition(left, right, pivot_pointIndex)

        #if pivot is at the target index
        if pivot_pointIndex == k_closest:
            return

        #otherwise
        #if pivot comes after the target index
        #do sorting again in the section that comes before pivot_pointIndex
        elif k_closest < pivot_pointIndex:
            quickselect(left, pivot_pointIndex - 1, k_closest)

        #otherwise
        #if pivot comes before the target index
        #do sorting again in the section that comes after pivot_pointIndex
        else:
            quickselect(pivot_pointIndex + 1, right, k_closest)
        
        return

    #0-index: points[k - 1] would be the k - closest point
    quickselect(0, n - 1, k - 1)

    #points[ : k] = points[0], points[1], ... , points[k -1] -> k-closest points
    return points[ : k]
```

- Define a function, `quickselect`, which we are going to use for the input array, `points`.

What we are trying to do here, is to sort `points` in order of distance from origin of each point in `points`.

1. We pick a random index, `pivot_pointIndex` and sort the list, `points` in the ascending order of distance from origin.
2. If `pivot` happens to be on the exactly `k`th element (= `points[k - 1]`) after the sorting (= meaning, `pivot_pointIndex` is `k - 1`), sorting ends.
3. Else if, `pivot` happens to lie right to the `k`th element, do the sorting again.
    - This time, pick a new `pivot` among the elements left to the previous pivot.
4. Else if, `pivot` happens to lie left to the `k`th element, do the sorting again.
    - This time, pick a new `pivot` among the elements right to the previous pivot.
5. Continue 3 ~ 4 until `pivot_pointIndex` is perfectly `k - 1`
6. The return object, `points[ : k]`  is the k-closest points. 

#### Part 3.


```python
    #input values are pointIndex
    def partition(left: int, right: int, pivot_pointIndex: int) -> int:

        #pivot point's distance from origin
        pivot_dist = distance[pivot_pointIndex]

        #push pivot point to the end of the given section (left, right) of points
        #do not forget to change the dictionary of distances accordingly
        points[pivot_pointIndex], points[right] = points[right], points[pivot_pointIndex]
        distance[pivot_pointIndex], distance[right] = distance[right], distance[pivot_pointIndex]

        #sorting
        store_pointIndex = left
        for i in range(left, right):
            #if a points[i]'s distance from origin is smaller than that of pivot
            if distance[i] < pivot_dist:
                #swap points[i] with points[store_pointIndex
                #do not forget to change the dictionary of distances accordingly
                points[i], points[store_pointIndex] = points[store_pointIndex], points[i]
                distance[i], distance[store_pointIndex] = distance[store_pointIndex], distance[i]
                store_pointIndex += 1
        #end of for loop
        #all points with smaller distances will be located in points[0] ... points[store_pointIndex - 1]
        #pivot will be at points[right]

        #swap points[right] (= pivot) with points[store_pointIndex]
        #pivot will be points[sotre_pointIndex] with all smaller distance points to the left of itself
        points[right], points[store_pointIndex] = points[store_pointIndex], points[right]
        distance[right], distance[store_pointIndex] = distance[store_pointIndex], distance[right]

        #return the pointIndex of pivot 
        return store_pointIndex
```

So, how does the sorting work?

1. Take a `pivot_pointIndex` and get its distance.
2. Put `pivot` to the right end.
3. While traversing through `points[left : right]`, whenever an element's distance is less than that of `pivot`, push it to the left side of the list.

    - `store_index` is smaller than or equal to `i`.
    - At the end of the for loop and after running `points[right], points[store_pointIndex] = points[store_pointIndex], points[right]`, all the elements left to `pivot` has smaller distance than that of `pivot` and vice versa for all the elements to the right of `pivot` 

4. return the `pivot`'s index after sorting, `store_pointIndex`.


### Complexity Analysis:

Time Complexity: *O(n)* (it is known that the worst case scenario is negligible. In the worst case, it is O(n^2))

- quickselect algorithm

Space Complexity: *O(n)* 

- `distance`
- Instead of declaring a separate dictionary, we can instead calculate distances on the go. In this case, space complexity would be O(1)
