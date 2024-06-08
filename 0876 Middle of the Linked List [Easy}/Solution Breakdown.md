## 876. Middle of the Linked List

>Description: [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)\
Given the `head` of a singly linked list, return *the middle node of the linked list*.\
If there are two middle nodes, return **the second middle** node.


Constraints:

- The number of nodes in the list is in the range `[100, 300]`. 
- <code>1</sup> <= Node.val <= 10<sup>2</sup></code> 

### Solution: 

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```
### Breakdown of Solution:

**Two Pointers - Slow and Fast**

Make the fast pointer traverse the given linked nodes twice the speed of the slow pointer.

The slow pointer ends up pointing to the moddle nodes and the next pointers associated with it.

### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the length of the linked list

Space Complexity: *O(1)*

- storing pointer constants only