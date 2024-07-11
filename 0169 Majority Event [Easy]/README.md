## 0169. Majority Event

>Description: [0169. Majority Event](https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150)\
Given an array nums of size n, return the majority element.\
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Constraints:

- `n == nums.length`
- <code>1 <= nums.length <= 5*10<sup>4</sup></code> 
- <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code> 


### Solution: 

```python
def majorityElement(nums: list[int]) -> int:
    
    n = len(nums)
    #{number : count of the number}
    num_count = dict()

    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    #num: key
    #count: value
    for num, count in num_count.items():
        #You may assume that the majority element always exists in the array.
        #> (n/2) : majority
        if count > (n/2):
            return num 
```
### Breakdown of Solution:

**Counting using hash table**

While itereate all elements in a given array, store the frequency of appearance in a hash table.

Return the key with a value greater than `n/2`.

### Complexity Analysis:

Time Complexity: *O(n)*

- one for loop

Space Complexity: *O(n)*

- for hash table
