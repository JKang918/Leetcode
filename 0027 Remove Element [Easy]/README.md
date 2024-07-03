## 27. Remove Element

>Description: [27. Remove Element](https://leetcode.com/problems/remove-element/description/)\
Given an integer array `nums` and an integer val, remove all occurrences of val in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to val.

Consider the number of elements in `nums` which are not equal to val be k, to get accepted, you need to do the following things:

Change the array `nums` such that the first k elements of `nums` contain the elements which are not equal to val. The remaining elements of `nums` are not important as well as the size of `nums`.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

If all assertions pass, then your solution will be accepted.

Constraints:

- <code>1 <= nums.length <= 100</code>
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`


### Solution: 

```python
def removeElement(nums: list[int], val: int) -> int:    
    
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        # nums[j] = val:
            # i stays still, j traverses -> sliding window
```
### Breakdown of Solution 2:

**Two Pointers**

We start with the first element and traverse the given array. See whether the element is duplicate with `val`.

Whenever it is duplicate, sliding window opens up: `i` stays still with `j` increasing by one in the for loop.

When the new element distinct from `val` shows up, update `nums[i]` with it.

When the for loop ends, you end up with `nums[0] ... nums[i]` with distinct values. Return the number of distinct value, which is `i`.


### Complexity Analysis:

Time Complexity: *O(n)*

- iterate the array

Space Complexity: *O(1)*

- only constants
