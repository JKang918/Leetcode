## 170. Two Sum III - Data Structure Design

>Description: [170. Two Sum III - Data Structure Design](https://leetcode.com/problems/two-sum-iii-data-structure-design/description/)\
Check out the link above.

Constraints:

- <code>-10<sup>5</sup> <= number <= 10<sup>5</sup></code> 
- <code>-2<sup>31</sup> <= value  <= 2<sup>31</sup>-1</code> 
- At most <code>10<sup>4</sup></code> calls will be made to `add` and `find`.


### Solution: 

```python
from collections import defaultdict

class TwoSum:

    def __init__(self):
        self.TwoSum = []
        self.hashmap = defaultdict(int)

    def add(self, number: int) -> None:
        self.TwoSum.append(number)
        self.hashmap[number] += 1
        
    def find(self, value: int) -> bool:
        for num in self.TwoSum:
            if (value - num) in self.hashmap:
                #value - num == num: possibility of (a) pair(s) of identical number
                #but if self.hashmap[num] == 1: there is only one such number -> cannot form a pair of two identical numbers
                if value - num == num and self.hashmap[value - num] == 1:
                    continue
                #otherwise: pairs of different numbers
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
```
### Breakdown of Solution:

**Counting using hash table**

If `number` were all unique integers, hash set would have sufficed but in this problem we need to consider cases of duplicate numbers.

For a given integer, `num` in the array, we look for `value - num` in the counting hash map.

Tricky case is where `num` is equal to `value - num`. In this case, we check there are enough (more than or equal to 2) number of `num`. If there is only one `num` (which equals `value -num`), we cannot form a pair of identical numbers.\
This explains the nested `if statement` within the for loop in `find` function. 

### Complexity Analysis:

Time Complexity: *O(n)*

- one for loop

Space Complexity: *O(n)*

- for hash table
