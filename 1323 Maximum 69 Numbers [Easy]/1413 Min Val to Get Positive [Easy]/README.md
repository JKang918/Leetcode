## 1323. Maximum 69 Numbers [Easy]

>Description: [1323. Maximum 69 Numbers](https://leetcode.com/problems/maximum-69-number/description/)\
Check out the link above.   

Constraints:

- <code>1 <= num <= 10<sup>4</sup></code> 
- `num` consists of only `6` and `9` digits.

### Solution: 

```python
def maximum69Number (num: int) -> int:
    
    numstr = list(str(num))

    for i in range(len(numstr)):
        if numstr[i] == '6':
            numstr[i] = '9'
            break
    
    return int(''.join(numstr))
```
### Breakdown of Solution:

This problem is easily solvable if you are comfortable with using various python in-built functions.

- str(*e.g. int*): change data type to string
- list(*string*): parse string into characters and return a list of the characters
- for... break: first `6` -> change it to `9` and break out of the loop.
- `delimiter`.join(*string list*): join each character or words in a list of string with delimiter
- int(*e.g. string*): change data type to integer

### Complexity Analysis:

Time Complexity: *O(n)*

- conversion to string: O(n)
- conversion to list: O(n)
- traversing: O(n)
- joining: O(n)
- conversion to int: O(n)

Space Complexity: *O(n)*

- `numstr`