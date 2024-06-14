## 2351. First Letter to Appear Twice

>Description: [2351. First Letter to Appear Twice [Easy]](https://leetcode.com/problems/first-letter-to-appear-twice/description/)\
Given a string `s` consisting of lowercase English letters, return the first letter to appear twice.

Constraints:

- `s` consists of lowercase English letters.
- `2 <= s.length <= 100`
- `s` has at least one repeated letter.

### Solution: 

```python
def repeatedCharacter(s: str) -> str:
    seen = set()
    for char in s:
        if char not in seen: seen.add(char)
        else: return char

    #no need for return None here. s has at least one repeated letter
```
### Breakdown of Solution:

**using set for checking existence**

Instead of using brute force method to check whther each alphabet appears twice, use set function for O(1) search

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of `s`

Space Complexity: *O(n)*

- storing `seen`
