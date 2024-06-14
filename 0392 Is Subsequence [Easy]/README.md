## 392. Is Subsequence 

>Description: [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/description/)\
Given two strings s and t, return true if s is a subsequence of t, or false otherwise..


### Solution: 

```python
def isSubsequence(s: str, t: str) -> bool:
    
    i = j = 0

    while i < len(s) and j <len(t):
        if s[i] == t[j]:
            i += 1    
        j += 1
    
    return i == len(s)
```
### Breakdown of Solution:

**Two Pointers**

This problem is easily solved using two pointers.

Suppose s is not a substring of t. Then i never reaches the length of s, while pointer j for t increases regardless and eventually reaches len(t), ending the while loop.

### Complexity Analysis:

Time Complexity: *O(n)*

- *O(2n)* iterate s, iterate t

Space Complexity: *O(1)*

- store i and j
    
