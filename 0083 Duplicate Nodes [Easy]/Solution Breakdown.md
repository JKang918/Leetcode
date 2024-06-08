## 83. Duplicate Nodes [Easy]

>Description: [83. Duplicate Nodes [Easy]](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)\
Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return *the linked list **sorted** as well*.


Constraints:

- The number of nodes in the list is in the range `[0, 300]`. 
- <code>-10<sup>2</sup> <= Node.val <= 10<sup>2</sup></code> 
- The list is guaranteed to be **sorted** in ascending order.

### Solution: 

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    
    current = head
    while current and current.next:
        if current.next.val == current.val:
            current.next = current.next.next #remove duplicates
        else:
            current = current.next
    return head
```
### Breakdown of Solution:

**Two Pointers - Slow and Fast**

Take `current` as slow pointer and `current.next` as a fast one.

Check if they have the same values, meaning they are pointing at nodes with duplicate values.\
Then remove that duplicate nodes from the linked nodes.

Otherwise move forward until the fast pointer reaches the tail, ending the while loop.

### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the length of the linked list

Space Complexity: *O(1)*

- storing pointer constants only