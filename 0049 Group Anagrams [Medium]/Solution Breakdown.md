## 49. Group Anagrams

>Description: [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)\
Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.\
An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Constraints:

- <code>1 <= strs.length <= 10<sup>4</sup></code> 
- <code>0 <= strs[i].length <= 100</code> 
- `strs[i]` consists of lowercase English letters.

### Solution: 

```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    
    #dictionary {key -> sorted str / value -> list of original strings}
    lettdict = dict()
    
    for i in range(len(strs)):                                          #range(len(strs)) -> for every string in strs
        if "".join(sorted(list(strs[i]))) not in lettdict:              #parsing(list()) -> sorting(sorted()) -> sorted string("".join())
            lettdict["".join(sorted(list(strs[i])))] = [strs[i]]        #for key(sorted string) -> list of original strings (group of anagrams)
        else:
            lettdict["".join(sorted(list(strs[i])))].append(strs[i])
    
    #return dictionary values -> list of orginal strings with identical key (= grouped anagrams)
    return list(lettdict.values())
```
### Breakdown of Solution:

**Hash table**

Use the sorted string as each string's identifier.

For the same identifer, group all anagrams into a list and store this as dictionary value.

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of `str`

Space Complexity: *O(n)*

- storing `lettdict`
