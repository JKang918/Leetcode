## 1047. Remove All Adjacent Duplicates In String

>Description: [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)\
You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.\
We repeatedly make **duplicate removals** on `s` until we no longer can.\
Return *the final string after all such duplicate removals have been made*. It can be proven that the answer is **unique**.


Constraints:

- `s` consists of lowercase English letters.
- <code>1 <= s.length <= 10<sup>5</sup></code> 


### Solution: 

```python
def removeDuplicates(s: str) -> str:
    
    if len(s) == 1: return s
    
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:    #additional condition: not empty stack
            stack.pop()
        else:
            stack.append(s[i])

    return "".join(stack)                   #return string, not list(array)
```
### Breakdown of Solution:

Duplicate removal algorithm is a application of stack.

Remove duplicate by 1. not appending and 2. popping the stack.

To see wether removal is neccessary by using stack peek. `stack[-1]`

### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the length of the string

Space Complexity: *O(n)*

- storing `stack`
