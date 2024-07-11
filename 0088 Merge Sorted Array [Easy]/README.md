## 0088. Merge Two Sorted Arrays

>Description: [0088. Merge Two Sorted Arrays](https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150)\
Check out the link above.

Constraints:

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- <code>-10<sup>9</sup> <= nums1[i], nums2[j] <= 10<sup>9</sup></code> 

### Solution: 

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    ptr1 = m - 1
    ptr2 = n - 1
    ptr3 = m + n - 1

    while ptr1 >= 0 and ptr2 >= 0:
        if nums1[ptr1] > nums2[ptr2]:
            nums1[ptr3] = nums1[ptr1]
            ptr1 -= 1
            
        else: #nums2[ptr2] => nums1[ptr1]
            nums1[ptr3] = nums2[ptr2]
            ptr2 -= 1
        
        ptr3 -= 1

    #if nums2 is not exhausted
    if ptr1 == -1:
        while ptr2 >= 0:
            nums1[ptr3] = nums2[ptr2]
            ptr2 -= 1
            ptr3 -= 1

    #if nums1 is not exhausted -> no need for additional line

    return nums1
```
### Breakdown of Solution:

**Three Pointers**

Before begin, the below condition should be met:

- modify `nums1` inline.

And in acoordance with constraints, the length of `nums1` is `m + n`.

Because `nums1` and `nums2` are sorted in an ascending order, it would be convinient to iterate them from back to the front.

Set three pointers:

1. pointer1: start from the last element of `nums1`
2. pointer2: start from the last element of `nums2`, which is also the end of the array
3. pointer3: start from the end of `nums1`

Follow below procedures:

1. Until one of the pointers reach to the front of respective array, overwrite `nums1[ptr3]` with either `nums1[ptr1]` or `nums2[ptr2]`, whichever is greater.
2.1 When `ptr1 == -1`, in otherwords, when `ptr2` is pointing at a certain element in `nums2`, all the elements in `nums2`, from `nums2[0]` to `nums2[ptr2]`, should be overwritten to `nums[0]` ~ `nums[ptr3]`. Note that in this case `ptr3 == ptr2`.
2.2 When `ptr2 == -1`, in othrewords, when `ptr1` is pointing at a certain element in `nums1`, do nothing.
3. Return `nums1`

### Complexity Analysis:

Time Complexity: *O(n)*

- check the list with length of n

Space Complexity: *O(1)*