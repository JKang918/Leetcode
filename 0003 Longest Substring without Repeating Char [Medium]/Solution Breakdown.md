## 3. Longest Substring without Repeating Characters

>Description: [3. Longest Substring without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)\
Given a string `s`, find the length of the **longest substring**

Constraints:

- <code>0 <= s.length <= 10<sup>4</sup></code> 
- `s` consists of English letters, digits, symbols and spaces.

### Solution: 

```python

def lengthOfLongestSubstring(s: str) -> int:
    
    letset = set()
    ans  = 0
    left = 0
    
    for right in range(len(s)):

        while s[right] in letset:
            letset.remove(s[left])
            left += 1
            
        letset.add(s[right])
        ans = max(ans, right + 1 - left)
    
    return ans
```
### Breakdown of Solution:

**Hash Set & Sliding Window**

Declare an hash set to check duplicate characters.

Declare `left` and `right` to build sliding windows.

Let's take an example and see how the hash set and sliding windows are used.


| index   | 0       | 1       | 2       | 3     | 4 | 5 | 6 | 7 | 8 |
|:-------:|:-------:|:-------:|:-------:|:-----:|:---:|:---:|:---:|:---:|:---:|
| char | a       | b       | c       | b     | d | c | a | b | a |
|         |         |         |         | right |   |   |   |   |   |
|         | left -> | left -> | left || |       |   |   |   |   |   |

At the fourth iteration (`i = 3`), duplicate character (`b`) shows up.\
Because in the previous iteration, there are `a`, `b`, `c` in the hash set already. (`letset.add(s[right])`). So unlike the previous iterations, this time the while loop is tirggered.

In the first iteration in the while loop, remove `a` from the hash set. But still there remains duplicate character and the second iteration is triggered due to the triggering condition: `s[right] in letset:`. `left = 1` in the end of the iteration.

In the second iteration, remove `b` from the hash set and increment `left` to `2`. The third iteration does not occur.

The resultant sliding window is `cb` and the length of it is `2`, which is obtained with `right + 1 - left`.

`2` is smaller than the length of previous longest substring, `abc`, so `ans` is not updated.

The same goes for further iterations of `right`.


### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of `right` and `left`. O(2n)

Space Complexity: *O(m)* (m being equal to or less than the number of English letters, digits, symbols and spaces)

- the size of hash set