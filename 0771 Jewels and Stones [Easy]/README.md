## 771. Jewels and Stones

>Description: [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)\
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

Constraints:

- <code>1 <= jewels.length, stones.length <= 50</code> 
- `jewels` and `stones` consist of only English letters.
- All the characters of `jewels` are unique.

### Solution: 

```python

def numJewelsInStones(jewels: str, stones: str) -> int:

    jew = set(jewels)

    ans = 0
    for s in stones:
        if s in jew: ans += 1
    
    return ans
```
### Breakdown of Solution:

**Hash table**

This solution is easily comprehensible.

### Complexity Analysis:

Time Complexity: *O(n + m)*

- iteration of jewels and stones

Space Complexity: *O(k)* (k being equal to or less than 52)

- there are only 26 alphabets. 26 for Upper cases and lower cases respectively. 
