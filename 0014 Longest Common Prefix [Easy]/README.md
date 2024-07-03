## 0014. Longest Common Prefix

>Description: [0014. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)\
Write a function to find the longest common prefix string amongst an array of strings.\
If there is no common prefix, return an empty string `""`.


Constraints:

- <code>1 <= strs.length <= 200</code> 
- <code>0 <= strs[i].length <= 200</code> 
- `strs[i]` consists of only lowercase English letters.

### Solution 1  Horizontal Search: 

```python
def longestCommonPrefix(self, strs: list[str]) -> str:
    
    #take the first word as a common prefix
    prefix = strs[0]

    #compare this to all the others starting with the second word
    for i in range(1, len(strs)):
        
        #if the prefix exists in another word in a string list, then it will 0
        #because that phrase(prefix) if found at the beginning of the other word
        while strs[i].find(prefix) != 0:

            #because it is not a common prefix, let's reduce the given prefix by each letter at the end
            prefix = prefix[0: len(prefix) - 1]

            if prefix == "":
                return prefix

    return prefix
    
```
### Breakdown of Solution:

**Horizontal Search**

1. Assume the first string as a whole as common prefix
2. Check whether this is truly common prefix by comparing it with other strings in the list. If it's common, it should exist in the other strings and the find method should result in zero.
3. Whenever the `find` method results in non-zero (no common prefix), slice the last letter of the prefix away and check whether this sliced prefix is common using `while` loop.

### Complexity Analysis:

Time Complexity: *O(S)*

- *S* being the sum(total length) of all strings in the list.

Space Complexity: *O(1)*

- only constants



### Solution 2  Lexicographical Order: 

```python
def longestCommonPrefix(strs: list[str]) -> str:
    
    #lexicographical order
    strs.sort()

    ans = ""

    #only need to compare the first string and the last string
    #iterate for smaller of the two strings' lengths

    for i in range(min(len(strs[0]),len(strs[len(strs)-1]))):
        #if same letter
        if strs[0][i] == strs[len(strs)-1][i]:
            #append
            ans += strs[0][i]
        #if not same letter
        else:
            #just return
            return ans
    #if identical -> return 
    return ans

```
### Breakdown of Solution:

Specific to this problem, the special solution using lexicographical order nature of string `sort` method.

When stort method is applied to a list of strings, it sorts its elements in lexicographical order.

Therefore, to find the logest common prefix, only the first and the last strings can be compared. 


### Complexity Analysis:

Time Complexity: *O(S)*

- *S* being the length of either the first or the last string. This exceptionally improves time complexity compared to horizontal search method. You don't need to go through other strings.

Space Complexity: *O(1)*