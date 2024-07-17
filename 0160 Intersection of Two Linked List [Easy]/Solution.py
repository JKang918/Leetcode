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