## 203. Remove Linked List Elements

>Description: [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)\
check out the link above

Constraints:

- The number of nodes in the list is in the range <code> [0, 10<sup>4</sup>]</code> .
- `1 <= Node.val <= 50`
- `0 <= val <= 50`

### Solution: 

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    
    prev = ListNode()
    prev.next = head

    dummy = prev

    ptr = head

    while ptr:
        if ptr.val == val:
            prev.next = ptr.next
        else:
            prev = prev.next
        ptr = ptr.next
    
    return dummy.next
```
### Breakdown of Solution:

**Dummy Node**

Focus on `prev` and `ptr`

Define previous pointer as an empty node and connect it to `head`.

`ptr` is a node pointer starting at `head`.

While traversing through the linked list, 

    1. no event -> just traverse the linked list
    2. event -> remove the node by connecting the previous node to the `ptr.next` node

At the end, we have to return the whole, possibly modifed, list.

You might be tempted to return `head` and it would not cause problem in most cases.

However, in case when the head node itself should be removed, it causes some issues.

To get around with that problem, declare `dummy`. Even when original `head` is removed, dummy.next will point to new `head`.


### Complexity Analysis:

Time Complexity: *O(n)*

- check all nodes

Space Complexity: *O(1)*

- constants