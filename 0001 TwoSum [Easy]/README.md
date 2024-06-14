## 0001. Two Sum

>Description: [0001. Two Sum](https://leetcode.com/problems/two-sum/description/)\
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.\
You may assume that each input would have exactly one solution, and you may not use the same element twice.\
You can return the answer in any order.

Constraints:

- <code>2 <= nums.length <= 10<sup>4</sup></code> 
- <code>10<sup>-9</sup> <= nums[i], target <= 10<sup>9</sup></code> 

### Solution 1  Burte Force: 

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    
    for i in range(len(nums) - 1):          #from 1st to (len(nums) - 1)th
        for j in range(i + 1, len(nums)):   #from 2nd to (len(nums))th
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
### Breakdown of Solution:

**checking all pairs**

One intuitive approach would be checking all possible pairs.

Note that it generates all pairs using nested for loop.

### Complexity Analysis:

Time Complexity: *O(n<sup>2</sup>)*

- nested for loop

Space Complexity: *O(1)*



### Solution 2  Hash map: 

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    
def twoSum(nums: list[int], target: int) -> list[int]:
    htable = dict()
    
    for i in range(len(nums)):
        if (target - nums[i]) in htable:
            return [htable[target - nums[i]], i]
        htable[nums[i]] = i
    return []
```
### Breakdown of Solution:

**Checking for existence using hash table**

To avoid using nested for loop, we can instead use hash table with key of elements in `nums` and values of their indices.

For a certain element, `nums[i]` in a given iteration, what you need to search in the hash map is the value(index) of the key, `target - nums[i]`, which when added to the `nums[i]` makes the sum the target.

This search costs O(1) time complexity

### Complexity Analysis:

Time Complexity: *O(n)*

- one for loop

Space Complexity: *O(n)*

- for hash table
