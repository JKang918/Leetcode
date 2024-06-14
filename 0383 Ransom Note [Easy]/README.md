## 383. Ransom Note

>Description: [383. Ransom Note](https://leetcode.com/problems/ransom-note/description/)\
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.\
Each letter in `magazine` can only be used once in `ransomNote`.

Constraints:

- <code>1 <= ransomNote.length, magazine.length <= 10<sup>5</sup></code> 
- `ransomNote` and `magazine` consist of lowercase English letters.

### Solution: 

```python

def canConstruct(ransomNote: str, magazine: str) -> bool:
    
    #improve speed
    if len(ransomNote) > len(magazine): return False

    charcount = dict()

    for char in magazine:
        charcount[char] = charcount.get(char, 0) + 1
    
    for char in ransomNote:
        if charcount.get(char, 0) == 0: return False
        else:
            charcount[char] -= 1
    
    return True
```
### Breakdown of Solution:

**Hash table**

Create hash table -> {'character' : 'frequency'}

subtract the count(frequency) everytime the same character appears in ransomnote.

If such character is nonexistent or occurrs more time in ransomenote -> False

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of magazine(n) and ransomeNote(m). n is greater than m.

Space Complexity: *O(k)* (k being equal to or less than 26)

- there are only 26 alphabets
