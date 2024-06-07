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

#example
# head = [3, 2, 0, -4]
one = ListNode(3)
two = ListNode(2)
three = ListNode(0)
four = ListNode(-4)
one.next = two
two.next = three
three.next = four
four.next = two #cycle: from -4 to 2
head = one
print(hasCycle(head)) # True <- there is a cycle