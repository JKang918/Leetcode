## 160. Intersection of Two Linked Lists

>Description: [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)\
Check out the link above.

Constraints:

- The number of nodes of `listA` is in the `m`.
- The number of nodes of `listB` is in the `n`.
- <code>1<sup>5</sup> <= m, n <= 10<sup>4</sup></code> 
- <code>1<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>
- `0 <= skipA < m`
- `0 <= skipB < n`
- `intersectVal` is `0` if `listA` and `listB` do not intersect.
- `intersectVal == listA[skipA] == listB[skipB]` if `listA` and `listB` intersect.

### Solution: 

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:

    ptr1 = headA
    ptr2 = headB

    nodes = set()

    while ptr1:
        nodes.add(ptr1)
        ptr1 = ptr1.next
    
    while ptr2:
        if ptr2 not in nodes:
            ptr2 = ptr2.next
        else:
            return ptr2
    
    return None
```
### Breakdown of Solution:

**Hash Set**

Store in a set all the nodes in one linked list.

First time they interesect, return that intersecting node. This is expressed in the below code:

```python

    while ptr2:
        if ptr2 not in nodes:
            ptr2 = ptr2.next
        else: #when intersecting point
            return ptr2
```

When there is no intersection, the second while loop will end and the solution will return `None`.

### Complexity Analysis:

Time Complexity: *O(n)*

- traversing two linked lists

Space Complexity: *O(1)*

- storing pointer constants only
