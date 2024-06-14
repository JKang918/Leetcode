## 2390. Removing Stars From a String

>Description: [2390. Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/)\
Check out the link above for description and examples.

Constraints:

- <code>1 <= s.length <= 10<sup>5</sup></code> 
- `s` consists of lowercase English letters and stars `*`.
- The operation above can be performed on `s`.


### Solution: 

```python
def removeStars(s: str) -> str:
    stack = []
    for char in s:
        if char == "*":
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

 
```
```

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

```

### Breakdown of Solution:

**Stack**

Note:

- LIFO <- see that when `*` comes up the previous letter should be popped out and be gone. This gives a perfect application ground for the data structure: stack
- Traverse through the string. No `*`, then push. If `*` comes along then pop the top.


### Complexity Analysis:

Time Complexity: *O(n)*

- iterate `s`

Space Complexity: *O(n)* 

- max of `stack`
    
