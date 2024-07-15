## 205. Isomorphic Strings

>Description: [141. Linked List Cycle](https://leetcode.com/problems/isomorphic-strings/description/)\
Check out the link above.

Constraints:

- <code>t.length == s.length</code> 
- <code>1</sup> <= s.length  <= 5*10<sup>4</sup></code> 
- `s` and `t` consist of any valid ascii character.

### Solution: 

```python
def isIsomorphic(s: str, t: str) -> bool:
    
    #two-way mapping
    map_s_to_t = dict()
    map_t_to_s = dict()

    #first check they are same length
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        
        #when char in s is already seen
        if s[i] in map_s_to_t:
            #check whether the matching char in t is correct
            if map_s_to_t[s[i]] != t[i]:
                return False
        
        #vice versa for t
        if t[i] in map_t_to_s:
            if map_t_to_s[t[i]] != s[i]:
                return False

        #first match
        map_s_to_t[s[i]] = t[i]
        map_t_to_s[t[i]] = s[i]
    
    return True
```
### Breakdown of Solution:

**Two Hash Maps**

map each pair of corresponding characters in respective strings in two dictionaries.

If the same character comes up in either one of the strings and its corresponindg match is inconsistent with previous match, return False.

### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the lengths of strings

Space Complexity: *O(n)*

- for dictionaries (hash maps)
