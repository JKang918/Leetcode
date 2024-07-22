## 136. Single Number

>Description: [136. Single Number](https://leetcode.com/problems/single-number/description/)\
Check out the link above

Constraints:
 
- <code>1 <= nums.length <= 3 * 10<sup>4</sup></code> 
- <code>-3 * 10<sup>4</sup> <= nums[i] <= 3 * 10<sup>4</sup></code> 
- Each element in the array appears twice except for one element which appears only once.


### Solution 1. Bitmask, XOR: 

```python
from typing import List

def singleNumber(self, nums: List[int]) -> int:
    a = 0
    for i in nums:
        a ^= i
    return a
```
### Breakdown of Solution 1. XOR:

**Bitmask XOR operation**

XOR operation explained:

Let's say we have two integers and we convert them to binary.

When we apply the XOR operation between them, for each corresponding bit, if 1 appears exactly once, the output is 1; otherwise, the output is 0.

For example, 

- 1100 (XOR) 1100 = 0000,
- 1111 (XOR) 1100 = 0011,
- and 1010 (XOR) 0000 = 1010.

Therefore, the following relationships hold:

$$a \oplus 0 = a$$

If we take XOR of two same bits, it will return 0:

$$a \oplus a = 0$$

Using the properties above, we can show:

$$a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b$$

Also, you can see that commutative property holds as well.

We assumed all input integers in the input list are duplicate, except 1.

If we apply XOR operation to all of the integers, duplicate ones will cancel out and only the target integer will be left.


### Complexity Analysis:

Time Complexity: *O(n)*

- iterate through `nums`

Space Complexity: *O(1)*

- constants only

---


### Solution 2. Math and hash set: 

```python
from typing import List

def singleNumber(self, nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
    
    return (2*sum(seen)) - sum(nums)
```
### Breakdown of Solution 2.:

**hash set**

Traverse the list to sort out distinct set of integers.

Twice the sum of distinct integers will be greater than the sum of the input array by the target integer.

### Complexity Analysis:

Time Complexity: *O(n)*

- iterate through `nums`

Space Complexity: *O(n)*

- hash set


---

### Solution 3. hash set: 

```python
from typing import List

def singleNumber(nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            seen.remove(num)
    
    for e in seen:
        return e
```
### Breakdown of Solution 2.:

**hash set**

Traverse the list to sort out distinct set of integers.

Whenever the already seen integer comes along, remove it from the hash set.

At the end, there will be only the target integer in the hash set. Return that.

### Complexity Analysis:

Time Complexity: *O(n)*

- iterate through `nums`

Space Complexity: *O(n)*

- hash set
