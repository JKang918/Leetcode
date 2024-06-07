## 141. Linked List Cycle

>Description: [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)\
Given head, the `head` of a linked list, determine if the linked list has a cycle in it.\
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that pos is not passed as a parameter.**\
Return *`true` if there is a cycle in the linked list*. Otherwise, return `false`.

Constraints:

- <code>The number of the nodes in the list is in the range [0, 10<sup>4</sup>].</code> 
- <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code> 
- `pos` is `-1` or a **valid index** in the linked-list.

### Solution: 

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow: return True
    return False
```
### Breakdown of Solution:

**Two Pointers - Slow and Fast**

If there is a cycle in a singly linked list, `fast` pointer eventually catch up with the `slow` pointer. In this case return `True`, oterwise return `False`.

### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the length of the linked list

Space Complexity: *O(1)*

- storing pointer constants only
