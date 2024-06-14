## 71. Simplify Path

>Description: [71. Simplify Path](https://leetcode.com/problems/simplify-path/description/)\
The description is quite long with useful examples, so advise you to click the link and check yourself.


Constraints:

- <code>1 <= path.length <= 3000</code> 
- `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`.
- `path` is a valid absolute Unix path.


### Solution: 

```python
def simplifyPath(path: str) -> str:
    path = path.split('/')
    
    stack = []

    #Forloop
    for char in path:

        #first slash
        if char == '' and not stack:
            stack.append(char)

        # Multiple consecutive slashes -> no push
        elif char == '':
            None

        # One lvl up is impossible
        elif char == '..' and stack[-1] == '':
            None

        # One lvl up -> pop to move up a directory
        elif char == '..' and stack[-1] != '':
            stack.pop()    
        
        # Current directory -> no push
        elif char == '.':
            None
            
        #normal cases, including '...' or '_'
        else:
            stack.append(char)    

    #Forloop Ends

    
    # if the end result is '/'
    if stack == ['']: return '/'

    #otherwise, join them with '/' as the delimiter
    else:             return '/'.join(stack)
```
### Breakdown of Solution:

**Stack**

Stack is particulary useful in this problem.

```
Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level.
```

Cehck out the above. Suppose all the directories can be stored in the stack as `[home, user, Documents, Pictures]`\
To move up a directory, before adding `Pictures`, pop `Documents` and only then add it. This makes this problem conducive to using stack.

Other codes are there to check for other rules.

Note that `split` method and `join` method are used frequently with `strings`.\
`split` method is useful when traversing a given string word by word.\
If it were to be letter to letter, `list(string)` would have been used.

### Complexity Analysis:

Time Complexity: *O(n)*

- linear to the length of the input

Space Complexity: *O(n)*

- storing `stack`
