## 290. Word Pattern

>Description: [290. Word Pattern](https://leetcode.com/problems/word-pattern/)\
Check out the link above.

Constraints:

- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s`  contains only lowercase English letters and spaces ' '.
- `s` does not contain any leading or trailing spaces.
- All the words in `s` are separated by a single space.

### Solution: 

```python
def wordPattern(pattern: str, s: str) -> bool:
    s = str.split(s)
    patt_to_word = dict()
    word_to_patt = dict()
    
    if len(pattern) != len(s):
        return False
    
    for char, word in zip(pattern, s):
        
        if char in patt_to_word:
            if patt_to_word[char] != word:
                return False
        
        if word in word_to_patt:
            if word_to_patt[word] != char:
                return False

        #first one-to-one match
        patt_to_word[char] = word
        word_to_patt[word] = char
    
    return True
```
### Breakdown of Solution:

**Two Hash Maps**

map each pair of corresponding character - word / word - character in respective strings in two dictionaries.

If a previously seen character or word comes up and the matching word or character is different from previous results, return False

### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the lengths of strings

Space Complexity: *O(n)*

- for dictionaries (hash maps)
