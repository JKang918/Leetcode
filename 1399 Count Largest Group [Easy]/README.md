## 1399. Count Largest Group [Easy]

>Description: [1399. Count Largest Group](https://leetcode.com/problems/count-largest-group/)\
Check out the link above.   

Constraints:

- <code>1 <= n <= 10<sup>4</sup></code> 

### Solution: 

```python
from collections import defaultdict

def countLargestGroup(n: int) -> int:

    digits = defaultdict(int)
    
    
    def sumDigits(a: int) -> int:
        sumdig = 0
        while a > 0:
            sumdig += a % 10
            a = a // 10
        return sumdig
    

    for k in range(n):
        sumdig = sumDigits(k + 1)
        digits[sumdig] += 1
    
    size = max(digits.values())
    
    # Count the number of groups with the largest size
    count = sum(1 for count in digits.values() if count == size)
    
    return count
```
### Breakdown of Solution:

Traverse from 1 to n.

Calculate sum of digits for an integer k in the range: [1 : n]

Create a hashmap of keys and values where keys are sums of digits and values are count of each sum of digit.

`size` is the maximum frequency of sums of digits.

Whenever a give sum of digits is the most frequently observed one, `count += 1`.

### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- traversal: O(n)
- sum of digits: O(log n)
- total: O(n log(n))

Space Complexity: *O(n)*

- `digits`