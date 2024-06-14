## 844. Backspace String Compare

>Description: [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/description/)\
Given two strings `s` and `t`, return `true` *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.\
Note that after backspacing an empty text, the text will continue empty.


Constraints:

- `s` and `t` only contain lowercase letters and `'#'` characters.
- <code>1 <= s.length, t.length <= 200</code> 


### Solution: 

```python
def buildingStack(s: str) -> str: #make it a function because the same process is repeated for s and t
    stack = []
    for c in s:
        if c != "#":
            stack.append(c)
        if c == "#" and stack:    #make sure it is not empty
            stack.pop()
    return "".join(stack)


def backspaceCompare(s: str, t: str) -> bool:
    
    return buildingStack(s) == buildingStack(t) 
```
### Breakdown of Solution:

When encountered during the iteration the character "#", do not append and pop the previous letter.

In case "#" at first, check whether the stack is empty first to prevent runtime error.

### Complexity Analysis:

Time Complexity: *O(n + m)*

- linearly correlated with the length of the string

Space Complexity: *O(n + m)*

- storing `stack`
