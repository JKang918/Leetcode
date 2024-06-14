## 970. Squares of Sorted Array 

>Description: [970. Squares of Sorted Array ](https://leetcode.com/problems/squares-of-a-sorted-array/description/)\
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


### Solution: 

```python
def sortedSquares(nums: list[int]) -> list[int]:

    #output array
    result = [0] * len(nums)
    
    #two pointers
    left  = 0
    right = len(nums) - 1
    
    for i in range(len(result)):
        if abs(nums[left]) > abs(nums[right]):
            #plug in from the right side
            result[len(result) - (i + 1)] = nums[left] ** 2
            left += 1
        else:
            #plug in from the right side
            result[len(result) - (i + 1)] = nums[right] ** 2
            right -= 1
    
    #No need
    #if left > right: break
    
    return result
```
### Breakdown of Solution:

**Two Pointers**

Note:

- additional sorting is not required: all elements are already sorted in ascending order
- if we take the absolute values of elements: left part(negative elements) is descending order and right part(positive elements) is ascending order

So taking a square of each element and sorting it can be said to be a trivial solution and inefficient as well.

Instead, we take the *two pointers* approach.\
Break apart the given array into two parts: negative part and positive part. And it can be seen that the elements with greatest absolute values are located at both ends. We compare these elemnts and plug them in the output array in the reverse order so that the larger squared elements are located on the right (ascending order).

There is no need to put the additional break condition, since the length of the output array is limited to `nums.length` in the first place. The for-loop ends before `left` becomes grater than `right`. 

### Complexity Analysis:

Time Complexity: *O(n)*

- iterate `nums`

Space Complexity: *O(n)* or *O(1)* 

- consider result then it is O(n). Otherwise, O(1)
    
