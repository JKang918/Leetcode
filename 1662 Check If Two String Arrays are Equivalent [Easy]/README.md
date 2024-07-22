## 1662. Check If Two String Arrays are Equivalent

>Description: [1662. Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/)\
Check out the link above.

Constraints:

- <code>-10<sup>3</sup> <= word1.length, word2.length <= 10<sup>3</sup></code> 
- <code>-10<sup>3</sup> <= word1[i].length, word2[i].length <= 10<sup>3</sup></code> 
- <code>-10<sup>3</sup> <= sum(word1[i].length), sum(word2[i].length) <= 10<sup>3</sup></code> 
- `word1[i]` and `word2[i]` consist of lowercase letters.

### Solution 1. concatenation: 

```python
from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    
    
    return ''.join(word1) == ''.join(word2)
```
### Breakdown of Solution:

**Concatenate each list of string**

Use python in-built function, `join` to concatenate both lists of strings.

Chekc whether they are indentical.

### Complexity Analysis:

Time Complexity: *O(n)*

- concatenating

Space Complexity: *O(n)*

- extra space for concatenated two strings


---

### Solution 2. parsing: 

```python
from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    
    list1 = []
    list2 = []

    for char in word1:
        list1.extend(char)
    
    for char in word2:
        list2.extend(char)
    
    return list1 == list2
```
### Breakdown of Solution:

**Parsing**

Parse each list of strings to build list of characters (one-length string).

Compare them.

### Complexity Analysis:

Time Complexity: *O(n)*

- parsing

Space Complexity: *O(n)*

- extra space for parsed lists

---

### Solution 3. one-way parsing: 

```python
from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    list2 = []
    
    for string in word2:
        list2.extend(string)
    
    word2len = len(list2)
    
    index = 0
    for string in word1:
        for char in string:
            if index == word2len or list2[index] != char:
                return False
            index += 1
    
    if index == word2len:
        return True
    
    return False
```
### Breakdown of Solution:

**Parsing**

Parse only one of the lists

Compare them.

### Complexity Analysis:

Time Complexity: *O(n)*

- parsing

Space Complexity: *O(n)*

- extra space for the parsed list (better than two parsing)

---

### Solution 4. no preprocessing: 

```python
from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    
    strIndex = 0
    charIndex = 0
    word2len = len(word2) #strIndex
    word2charlen = [len(string) for string in word2] #charIndex #this part is critical
    
    #traverse following each character in word1 
    for string in word1:
        for char in string:
            #either word2 is exhausted too early or not mathcing
            if strIndex == word2len or (char != word2[strIndex][charIndex]):
                return False
            
            charIndex += 1

            if charIndex == word2charlen[strIndex]:
                strIndex += 1
                charIndex = 0

    #word2 exhaustion check
    if charIndex != 0 or strIndex != word2len:
        return False
    
    return True
```

### Breakdown of Solution:

**Parsing**

Choose one list. In this case, I picked `word1`.

Traverse `word1` and check it with `word2` during traversal.

Because we are interested in each individual character in `word2` while `word2` being list of strings, we setup two indices.

1. `strIndex` to locate each string in the list
2. `charIndex` to locate each character in a certain string with index, `strIndex`

```python
if ... (char != word2[strIndex][charIndex]):
    return False
```

- find each character in `word1` and compare it the corresponding character in `word2`
- if not same, return `False`

```python
charIndex += 1

    if charIndex == word2charlen[strIndex]:
        strIndex += 1
        charIndex = 0
```

- After the check, if same, move charIndex to the next character within the selected string
- However, if the selected string is exhausted, move to the next string


```python
if strIndex == word2len or ....
...
#word2 exhaustion check
    if charIndex != 0 or strIndex != word2len:
        return False
```

- These two lines are to check the lengths of the two input lists.
- First, `strIndex == word2len` while still in the for loop means `word2` is already exhausted -> return `False`
- Second, after the for loop, if `word2` is **NOT** correspondingly exhuasted -> return `False`


### Complexity Analysis:

Time Complexity: *O(n)*

- traversing

Space Complexity: *O(n)*

- for `word2charlen`