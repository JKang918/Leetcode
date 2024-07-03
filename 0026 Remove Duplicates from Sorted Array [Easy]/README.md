## 26. Remove Duplicates from Sorted Array

>Description: [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)\
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first k elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return k.

Custom Judge:

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

Constraints:

- <code>1 <= nums.length <= 3*10<sup>4</sup></code>
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.


### Solution: 

```python
def removeDuplicates(nums: list[int]) -> int:

    ref = nums[0]

    #start with the second element
    i = 1
    while i < len(nums):
        if nums[i] == ref:
            nums.pop(i)
        else:
            ref = nums[i]
            i += 1
    
    return len(nums)
```
### Breakdown of Solution:

**Iteration**

```python
ref = nums[0]
```
Take the first element as a reference.

```python
#start with the second element
    i = 1
    while i < len(nums):
        if nums[i] == ref:
            nums.pop(i)
        else:
            ref = nums[i]
            i += 1
```

Check whether next coming elements are duplicates.

If one is duplicate, 1. pop that off from the array, 2. and check the same index again in the next iteration.

If not duplicate, then go on to the next element in the array and make it a new reference.


```python
    return len(nums)
```

At the end, you will end up with the array with distinct integers.\
Return the length of that array.


### Complexity Analysis:

Time Complexity: *O(n)*

- iterate the array

Space Complexity: *O(1)*

- only constants
