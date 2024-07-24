## 215. Kth Largets Element in an Array

>Description: [215. Kth Largets Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)\
Check out the link above

Constraints:

- <code>1 <= k <=> nums.length <= 10<sup>5</sup></code> 
- <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code> 

### Solution 1. Heap: 

```python
from typing import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:

    
    nums = [- num for num in nums]
    heapq.heapify(nums)

    for _ in range(k - 1):
        heapq.heappop(nums)
    
    return - heapq.heappop(nums)
```
### Breakdown of Solution:

**Heap**

First, modify the given list to turn all integers in the array to negative counterparts.

Second, convert the python list to python heap. Then, every time we heappop the heap, the largest absolute value will pop up.

Fourh, pop the heap `k` times. Return the `k`th popped integer. Do not forget to convert it to positive. 

### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- heapify, traversals

Space Complexity: *O(1)* 

- in python, heapifying does not take additional space.

---

### Solution 2. Quickselect (common): 

```python
from typing import List
import random

def findKthLargest(nums: List[int], k: int) -> int:

    
    def partition(left, right, pivot_index):
        
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store_index = left
        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        return store_index

    def quickselect(left, right, k_largest) -> None:
        
        if left == right:
            return
        
        pivot_index = random.randint(left, right)

        pivot_index = partition(left, right, pivot_index)

        if pivot_index == k_largest:
            return
        elif pivot_index > k_largest:
            quickselect(left, pivot_index - 1, k_largest)
        else:
            quickselect(pivot_index + 1, right, k_largest)
        
        return

    n = len(nums)
    quickselect(0, n - 1, k - 1)
    return nums[k - 1]        
```
### Breakdown of Solution:

**Quickselect Algorithm**

*Before we begin, Note that in this particular leetcode problem, the above solution will not pass some test cases and lead to Time Limit Exceeded.*

The [leetcode editorial](https://leetcode.com/problems/top-k-frequent-elements/editorial/) provides excellent explanation as to the underlying mechanism of quickselect algorithm.

Here I explain mainly how each line works in the code implementation.


#### Part 1.

```python
    def quickselect(left, right, k_largest) -> None:
        
        if left == right:
            return
        
        pivot_index = random.randint(left, right)

        pivot_index = partition(left, right, pivot_index)

        if pivot_index == k_largest:
            return
        elif pivot_index > k_largest:
            quickselect(left, pivot_index - 1, k_largest)
        else:
            quickselect(pivot_index + 1, right, k_largest)
        
        return

    n = len(nums)
    quickselect(0, n - 1, k - 1)
    return nums[k - 1]       
```

- Define a function, `quickselect`, which we are going to use for `nums`.

What we are trying to do here, is to sort `nums` in descending order.

1. We pick a random element, `pivot` and sort the list, `nums` in descending order.
2. If `pivot` happens to be on the exactly `k`th largest element after sorting, sorting ends.
3. Else if, `pivot` happens to be lie right to the `k`th largest element, do the sorting again.
    - This time, pick a new `pivot` among the elements left to the previous pivot.
4. Else if, `pivot` happens to be lie left to the `k`th largest element, do the sorting again.
    - This time, pick a new `pivot` among the elements right to the previous pivot.
5. Continue 3 ~ 4 until `pivot_index` is perfectly `k - 1`, so that `nums[k - 1]` would be `k`th largest element. 
6. Return `nums[k - 1]`, `k`th largest element

#### Part 2.



```python
    def partition(left, right, pivot_index):
        
        #1. Take a `pivot_index` and take the value of `nums[pivot_index]`.
        pivot_value = nums[pivot_index]

        #2. Put `pivot` to the right end.
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        #3. While traversing `nums[left : right]`, whenever an element is larger than `pivot_value`, push it to the left side of the list.
        store_index = left
        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        # At the end of the for loop and after running `nums[store_index], nums[right] = nums[right], nums[store_index]`, all the elements left to `pivot` is larget than `pivot` and vice versa for all the elements right to `pivot`. 
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        #4. return the `pivot`'s index after sorting, `store_index`
        return store_index
```

So, how does the sorting work?

1. Take a `pivot_index` and take the value of `nums[pivot_index]`.
2. Put `pivot` to the right end.
3. While traversing `nums[left : right]`, whenever an element is larger than `pivot_value`, push it to the left side of the list.

    - `store_index` is smaller than or equal to `i`.
    - At the end of the for loop and after running `nums[store_index], nums[right] = nums[right], nums[store_index]`, all the elements left to `pivot` is larget than `pivot` and vice versa for all the elements right to `pivot`. 

4. return the `pivot`'s index after sorting, `store_index`


### Complexity Analysis:

Time Complexity: *O(n)* (it is known that the worst case scenario is negligible. In the worst case, it is O(n^2))

- quickselect algorithm

Space Complexity: *O(1)* 

- constants only

---

### Solution 3. Quickselect (less common): 

```python
from typing import List
import random

def findKthLargest(nums: List[int], k: int) -> int:

    def quickselect(nums, k):

        pivot = random.choice(nums)

        left, mid, right = [], [], []

        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)
        
        if len(left) >= k:
            return quickselect(left, k)
        
        if (len(left) + len(mid)) < k:
            return quickselect(right, k - (len(left) + len(mid)))
        
        return pivot

    return quickselect(nums, k)
```

### Breakdown of Solution:

**Quickselect Algorithm**

The [leetcode editorial](https://leetcode.com/problems/kth-largest-element-in-an-array/editorial/) provides excellent explanation as to the underlying mechanism of quickselect algorithm.

Here I explain mainly how each line works in the code implementation.


- Define a function, `quickselect`, which we are going to use for `nums`.

What we are trying to do here, is to sort `nums` in descending order.

1. We pick a random element, `pivot`.
2. Traverse `nums`. If a `num` in nums is smaller than `pivot`, put it in `left`. If it is larger than `pivot`, put it in `right`. Otherwise, put it in `mid`.
3. Check the length of `left` and `right`.

    1) if `len(left)` is greater than or equal to `k`, this means `k`th largets number is in `left`. So we picked the wrong pivot at first. Do the quickselect again for elelemtns in `left`.
    2) if `len(left) + len(mid)` is smaller than `k`, this means `k`th largest number is in `right`. So we picked the wrong pivot at first. Do the quickselect again for elements in `right`.
        - Be sure that in this new quickselect, we are looking for `k - (len(left) + len(mid))`th largest number. Becasue `(0, 1, ... , len(left) + len(mid))`th elements are already found.
    3) Otherwise, we picked the right `pivot`. Return `pivot`.
