# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    prev = None
    curr = head
    start = head.next


    while curr and curr.next:
        if prev:
            prev.next = curr.next
        prev = curr
        
        temp = curr.next.next
        curr.next.next = curr
        curr.next = temp
        curr = curr.next

    return start