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