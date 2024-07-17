## 242. Valid Anagram

>Description: [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)\
Check out the link above for detailed description.

Constraints:

- <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code> 
- `s` and `t` consist of lowercase English letters.


### Solution 1 sorting: 

```python
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```
### Breakdown of Solution:

Sort two strings lexicographically.

If they are identical, they are anagrams.

### Complexity Analysis:

Time Complexity: *O(nlog(n))*

- sorting

Space Complexity: *O(1)*

- none

### Solution 2.1. two hash maps: 

```python
def isAnagram(s: str, t: str) -> bool:
 
    hash1 = dict()
    hash2 = dict()

    for char in s:
        if char not in hash1:
            hash1[char] = 1
        else:
            hash1[char] += 1
    
    for char in t:
        if char not in hash2:
            hash2[char] = 1
        else:
            hash2[char] += 1
    
    return hash1 == hash2
```
### Breakdown of Solution:

Declare two hash maps for each string.

Count each character in each string.

If two hash maps are identical, they are anagrams.

### Complexity Analysis:

Time Complexity: *O(n)*

- traverse two strings

Space Complexity: *O(n)*

- two hash maps


### Solution 2.2. one hash map: 

```python
def isAnagram(s: str, t: str) -> bool:
 
    hash1 = dict()
    hash2 = dict()

    for char in s:
        if char not in hash1:
            hash1[char] = 1
        else:
            hash1[char] += 1
    
    for char in t:
        if char not in hash2:
            hash2[char] = 1
        else:
            hash2[char] += 1
    
    return hash1 == hash2
```
### Breakdown of Solution:

Declare a hash map for both string.

For char in s, count += 1\
For char in t, count -= 1

All dictionary values should be zero for anagrams.

### Complexity Analysis:

Time Complexity: *O(n)*

- traverse two strings

Space Complexity: *O(n)*

- one hash map
