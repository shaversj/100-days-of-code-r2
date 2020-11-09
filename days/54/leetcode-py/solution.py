# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        values = ""
        while curr:
            values += str(curr.val)
            curr = curr.next

        return int(values, 2)