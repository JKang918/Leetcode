## 347. Top K Frequent Elements

>Description: [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)\
Check out the link above

Constraints:

- <code>1 <= nums.length <= 10<sup>5</sup></code> 
- <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code> 
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

### Solution 1. Heap: 

```python
from typing import List
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    #freq: {each num in nums : counts}
    freq = dict()

    for e in nums:
        if e not in freq:
            freq[e] = 1
        else:
            freq[e] += 1
    
    heap = []
    ans = []
    for key, value in freq.items():
        heap.append((-value, key))

    heapq.heapify(heap)
    
    i = 0
    while i < k:
        x, y = heapq.heappop(heap)
        ans.append(y)
        i += 1

    return ans
```
### Breakdown of Solution:

**Heap**

First, create a dictionary to store frequency information for each unique integer in the input array. There are distinct integers with their respective frequency in the dictionary.

Second, traverse the dictionary: return frequncy(value) and distinct integer(key) into a list of tuples. Note that we changed the sign to negative for simulating max heap. (heapq does not support max heap)

Third, convert the python list to python heap. Then, every time we heappop the heap, the smallest value (greatest absolute value -> greatest frequency) will pop up.

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

def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    #freq: {each num in nums : counts}
    #unique: [each distinct num in nums]

    freq = dict()

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    unique = list(freq.keys())

    ###
    def partition(left: int, right: int, pivot_index: int) -> int:

        #get the frequency of the selected pivot element
        pivot_frequency = freq[unique[pivot_index]]

        #put pivot at the end of the to-be sorted list
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        #iterate from the leftmost element and compare its frequency to that of pivot
        #whenever less frequent element comes up, push it to the left 
        
        store_index = left
        for i in range(left, right):
            #if ith element's frequency is less than that of pivot
            if freq[unique[i]] < pivot_frequency:
                #swap ith element and store_index element                    
                unique[i], unique[store_index] = unique[store_index], unique[i]
                
                #note that i increases regardless but store_index increases only when if statement is run
                store_index += 1
        
        #move pivot (unique[right]) to store_index
        #now, all elements to the left is less frequent than pivot
        unique[right], unique[store_index] = unique[store_index], unique[right]

        #return the index of pivot
        return store_index


    def quickselect(left: int, right: int, k_smallest: int) -> None:

        #base case: the list contains only one element
        if left == right:
            return
        
        #pick a random index for pivot in unique
        pivot_index = random.randint(left, right)

        #Find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return
        
        #if pivot is (k+1), ... (k+..) smallest
        elif k_smallest < pivot_index:
            #than gotta find less frequent index
            quickselect(left, pivot_index - 1, k_smallest)
        
        #if pivot is (k-1), ... , (k- ...) smallest
        elif k_smallest > pivot_index:
            #then gotta find more frequent index
            quickselect(pivot_index + 1, right, k_smallest)
        
        return

    n = len(unique)
    quickselect(0, n - 1, n - k)
    

    return unique[n - k:]
```
### Breakdown of Solution:

**Quickselect Algorithm**

The [leetcode editorial](https://leetcode.com/problems/top-k-frequent-elements/editorial/) provides excellent explanation as to the underlying mechanism of quickselect algorithm.

Here I explain mainly how each line works in the code implementation.


#### Part 1.

```python
    #freq: {each num in nums : counts}
    #unique: [each distinct num in nums]

    freq = dict()

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    unique = list(freq.keys())
```

- Construct dictionary, `freq`, to store information about the distinct integers and their respective frequency. 
- Construct `unique`, a python list to store all the distinct integers.

#### Part 2.

```python

    def quickselect(left: int, right: int, k_smallest: int) -> None:

        #base case: the list contains only one element
        if left == right:
            return
        
        #pick a random index for pivot in unique
        pivot_index = random.randint(left, right)

        #Find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return
        
        #if pivot is (k+1), ... (k+..) smallest
        elif k_smallest < pivot_index:
            #than gotta find less frequent index
            quickselect(left, pivot_index - 1, k_smallest)
        
        #if pivot is (k-1), ... , (k- ...) smallest
        elif k_smallest > pivot_index:
            #then gotta find more frequent index
            quickselect(pivot_index + 1, right, k_smallest)
        
        return
    
    n = len(unique)
    quickselect(0, n - 1, n - k)

    return unique[n - k:]

```

- Define a function, `quickselect`, which we are going to use for `unique`.

What we are trying to do here, is to sort `unique` in accordance with integer frequencies: in the ascending order of frequency.

1. We pick a random element, `pivot` and sort the list, `unique` in the ascending order of frequency.
2. If `pivot` happens to be on the exactly `n - k`th element after the sorting (= meaning, `pivot` is `(n - k)`th less frequent element. In other words, it is `k`th frequent element.), sorting ends.
3. Else if, `pivot` happens to be lie right to the `n - k` element, do the sorting again.
    - This time, pick a new `pivot` among the elements left to the previous pivot.
4. Else if, `pivot` happens to be lie left to the `n - k` element, do the sorting again.
    - This time, pick a new `pivot` among the elements right to the previous pivot.
5. Continue 3 ~ 4 until `pivot_index` is perfectly `n - k`
6. The return object, `unique[n - k:]` becomes the list of integers that are kth or more frequent elements

#### Part 3.



```python
    def partition(left: int, right: int, pivot_index: int) -> int:

        #get the frequency of the selected pivot element
        pivot_frequency = freq[unique[pivot_index]]

        #put pivot at the end of the to-be sorted list
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        #iterate from the leftmost element and compare its frequency to that of pivot
        #whenever less frequent element comes up, push it to the left 
        
        store_index = left
        for i in range(left, right):
            #if ith element's frequency is less than that of pivot
            if freq[unique[i]] < pivot_frequency:
                #swap ith element and store_index element                    
                unique[i], unique[store_index] = unique[store_index], unique[i]
                
                #note that i increases regardless but store_index increases only when if statement is run
                store_index += 1
        
        #move pivot (unique[right]) to store_index
        #now, all elements to the left is less frequent than pivot
        unique[right], unique[store_index] = unique[store_index], unique[right]

        #return the index of pivot
        return store_index
```

So, how does the sorting work?

1. Take a `pivot` and check its frequency.
2. Put `pivot` to the right end.
3. While traversing through `unique[left : right]`, whenever an element's frequency is less than that of `pivot`, push it to the left side of the list.

    - `store_index` is smaller than or equal to `i`.
    - At the end of the for loop and after running `unique[right], unique[store_index] = unique[store_index], unique[right]`, all the elements left to `pivot` has less frequency that `pivot` and vice versa for all the elements right to `pivot` 

4. return the `pivot`'s index after sorting, `store_index`.


### Complexity Analysis:

Time Complexity: *O(n)* (it is known that the worst case scenario is negligible. In the worst case, it is O(n^2))

- quickselect algorithm

Space Complexity: *O(n)* 

- `unique`, `freq`
