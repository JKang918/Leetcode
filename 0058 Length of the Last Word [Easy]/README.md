## 58. Length of the Last Word

>Description: [58. Length of the Last Word](https://leetcode.com/problems/length-of-last-word/)\
Given a string s consisting of words and spaces, return the length of the last word in the string.\
A word is a maximal substring consisting of non-space characters only.

Constraints:

- <code>1 <= s.length <= 10<sup>4</sup></code>
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.


### Solution 1: 

```python
def lengthOfLastWord(s: str) -> int:
    
    i = -1
    length = 0
    
    #remove all the spaces in the last part until the last word shows up
    while (-i) <= len(s) and s[i] == " ":
        i -= 1
    
    #Then count the letters in last word
    while (-i) <= len(s) and s[i] != " ":
        i -= 1
        length += 1
    
    return length
```
### Breakdown of Solution:

**Iteration from the back**

We iterate the given string from the back. 

1. First, iterate the spaces, if any, until we encounter the last word. This is represented in the first wile loop.

2. Second, iterate the last word until we encounter space. The length of the word is counted in `length`.

### Complexity Analysis:

Time Complexity: *O(n)*

- iterate the string

Space Complexity: *O(1)*

- only constants



### Solution 2: 

```python
def lengthOfLastWord(s: str) -> int:
    
    s = str.split()
    
    return len(s[-1])
```
### Breakdown of Solution:

**Built-in function, str.split()**

string split method parse the given string into words.

Return the length of the last word, `s[-1]`.

### Complexity Analysis:

Time Complexity: *O(n)*

- time complexity of the built-in function

Space Complexity: *O(n)*

- space complexity of the built-in function