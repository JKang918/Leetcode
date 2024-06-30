## 0013. Roman to Integer

>Description: [0013. Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/)\

Roman numerals are represented by seven different symbols: `I, V, X, L, C, D and M.`

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. \
X can be placed before L (50) and C (100) to make 40 and 90. \
C can be placed before D (500) and M (1000) to make 400 and 900.\
Given a roman numeral, convert it to an integer.

Constraints:

- <code>1 <= s.length <= 15</code> 
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M').`
- It is guaranteed that s is a valid roman numeral in the range `[1, 3999]`.

### Solution 1  From left ot right: 

```python
def romanToInt(s: str) -> int:
        
        #solution 1. left to right
    romantable = {
            "I" : 1,        #V, X
            "IV": 4,
            "IX": 9,
            "V" : 5,
            "X" : 10,       #L, C
            "XL": 40,
            "XC": 90,
            "L" : 50,
            "C" : 100,      #D, M
            "CD": 400,
            "CM": 900,
            "D" : 500,
            "M" : 1000
            }

    ans = 0 #output integer
    i = 0   #index
    while i < len(s):
        if i < len(s) - 1 and s[i:i+2] in romantable:
            ans += romantable[s[i:i+2]]
            i += 2
        else:
            ans += romantable[s[i]]
            i += 1

    return ans
```
### Breakdown of Solution:

1. Chek the pair of Roman numbers
2. If these are special cases (IV, IX, XL, XC, CD, CM), find that in the hash map and skip two.
3. Otherwise, add each integer corresponding to that Roman number 

### Complexity Analysis:

Time Complexity: *O(n)*

- check the string with length of n

Space Complexity: *O(1)*

- storing the hash map



### Solution 2  From right ot left: 

```python
def romanToInt(s: str) -> int:
        
        
    #solution 2. right to left
    romantable = {
            "I" : 1,        #V, X
            "V" : 5,
            "X" : 10,       #L, C
            "L" : 50,
            "C" : 100,      #D, M
            "D" : 500,
            "M" : 1000
            }
    
    #output integer
    ans = romantable[s[len(s) - 1]] #right most roman letter
    
    #going from back to front #starting from the second letter from the right
    for right in range(1, len(s)):
        # if romantable[letter of interest] < romantable[letter to the right]
        if romantable[s[(len(s) - 1) - right]] < romantable[s[(len(s) - 1) - right + 1]]:
            ans -= romantable[s[(len(s) - 1) - right]]
        else:
            ans += romantable[s[(len(s) - 1) - right]]
    
    return ans
```
### Breakdown of Solution:

Based on the idea that those special cases only arise when the letter is smaller than the letter to its right.

So going from right to left, if a letter of interest is smaller than the one to its right, instead of adding it, subtract the corresponding integer.


### Complexity Analysis:

Time Complexity: *O(n)*

- going through a given string

Space Complexity: *O(1)*

- storing the hash map