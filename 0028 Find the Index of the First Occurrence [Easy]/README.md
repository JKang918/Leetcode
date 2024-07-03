## 28. Find the Index of the First Occurrence

>Description: [28. Find the Index of the First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)\
Given two strings `needle` and `haystack`, return the index of the first occurrence of needle in `haystack`, or -1 if `needle` is not part of `haystack`.

Constraints:

- <code>1 <= haystack.length, needle.length <= 10<sup>4</sup></code>
- `haystack` and `needle` consist of only lowercase English characters.


### Solution 1: 

```python
def strStr(haystack: str, needle: str) -> int:
    
    n = len(haystack)
    m = len(needle)
    
    #if m > n: no for loop at all
    for window in range(n - m + 1):
        for i in range(m):
            if needle[m] != haystack[window + m]:
                break
            if i == m - 1:                       #the key point of this solution
                return window
            
    
    return -1
    
```
### Breakdown of Solution:

**Two Pointers (Sliding Window)**

`needle` is the prefix we would like to search in `haystack`.

So the length of the sliding window we would like to search is the length of `needle`, `m`. This means the maximum the index of beginning element can get is `n - m`, hence `range(n - m + 1)`.

Whenever the first letter in the window does not match with the first letter in the `needle`, just move the sliding window.

However, if they match, search through the window with the inner for loop. If the inner for loop goes the full circle without hitting `break`, return `window`, the index of the beginning element of the window. 

Note that this is the emulation of the built-in `find` method. So simply typing:

```python
def strStr(haystack: str, needle: str) -> int:
    
    return haystack.find(needle)
```

gives you the same result.

### Complexity Analysis:

Time Complexity: *O(n)*

- iterate the array
- despite the nested for loop, each element iterates only onece (characteristic of sliding window algorithm)

Space Complexity: *O(1)*

- only constants
