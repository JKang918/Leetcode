## 21. Merge Two Sorted Lists

>Description: [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)\
You are given the heads of two sorted linked lists `list1` and `list2`.\
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.\
Return the head of the merged linked list.\


Constraints:

- The number of nodes in both lists is in the range `[0, 50]`.
- <code>-100 <= node.val <= 100</code> 
- Both `list1` and `list2` are sorted in non-decreasing order.


### Solution: 

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    dummy = ListNode(-1)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next
    
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next   
```
### Breakdown of Solution:

**Iteration**

```python
dummy = ListNode(-1)
```
Set up false `dummy` node to later comback to the head of the merged list.

```python
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next
```

Start with the list starting with a smaller value.

While traversing through a list, if smaller value is found on the other, switch to that with `current.next`. Note that `current` works as a "previous node".

Traversing ends if either one of the lists is exhasuted.

```python

    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next   
```

In that case, the `current` will be pointing at the last node of the exhausted list. Like that to the remaing nodes of the other list.

With returning `dummy.next` you return the whole merged list. 

### Complexity Analysis:

Time Complexity: *O(n + m)*

- iterate the given two lists

Space Complexity: *O(1)*

- only constants
