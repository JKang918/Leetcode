## 20. Valid Parentheses

>Description: [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)\
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.\
An input string is valid if:\
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


Constraints:

- `s` consists of parentheses only `'()[]{}'`.
- <code>1 <= s.length <= 10<sup>4</sup></code> 


### Solution: 

```python
def isValid(s: str) -> bool:
    
    paren = {'(' : ')', 
             '{' : '}', 
             '[' : ']'}
    
    stack = []

    for char in s:
        if char in paren:                    #opening parenthesis
            stack.append(char)
        else:                                #closing parenthesis
            if not stack:                    #in case it's an empty stack (exception)
                return False
            elif paren[stack.pop()] != char: #no matching
                return False
    
    if not stack: return True                #if all matched, at the end stack should be empty
    else: return False        
```
### Breakdown of Solution:

- Make a hash map with keys of opening parenthesis and values of closing parenthesis.

There is no intrinsic reason these parenthesis should all be in a single dictionary but it is more easy to read if done so.

- For each opening parenthesis in a given string, `s`, append it to the stack.

- For each closing parenthesis in a given string, `s`, pop the stack and see if that is matched with the closing parenthesis.
    - In case there is no matching prior parenthesis so the stack might be empty, check whether the stack is empty first.

- If the for loop ended with all matching parenthesis, the stack should be empty. If it is not, this means there are still some opening parentheses left in the stack.

### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the length of the string

Space Complexity: *O(n)*

- storing the dictonary and the stack
