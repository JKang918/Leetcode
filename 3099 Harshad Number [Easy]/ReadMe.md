## 3099. Harshad Number

>Description: [3099. Harshad Number](https://leetcode.com/problems/harshad-number/description/)\
Check out the link above for description and examples.

Constraints:

- `1 <= x <= 100`

### Solution 1 Converting to string: 

```python
def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
    

    sod = sum(int(digit) for digit in list(str(x)))
    
    if x % sod == 0:
        return sod
    else:
        return -1
```


### Breakdown of Solution:

**Converting to a string**

1. Covert given integer `x` 


### Complexity Analysis:

Time Complexity: *O(n)*

- iterate `s`

Space Complexity: *O(n)* 

- max of `stack`
    
