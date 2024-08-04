## 2696. Minimum String Length After Removing Substrings

>Description: [2696. Minimum String Length After Removing Substrings](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/)\
Check out the link above.

Constraints:

- `1 <= s.length <= 100`
- `s` consists only of uppercase English letters.


### Solution 

```python
def minLength(s: str) -> int:
    stack = []
    charmatch = {
        'A': 'B',
        'C': 'D'
    }

    for char in s:
        if stack and char == charmatch.get(stack[-1], 0):
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack)
```
### Breakdown of Solution:

**Stack**

Single pass over of the given array with for loop.

Whenever a match is found, pop the stack.

### Complexity Analysis:

Time Complexity: *O(n)*

- Single traversal

Space Complexity: *O(n)*

- `charmatch`