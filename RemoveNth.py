# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None

        cur_posn = head
        fast_posn = head

        for i in range(n):
            fast_posn = fast_posn.next

        if fast_posn is None:
            return head.next

        while fast_posn.next is not None:
            cur_posn = cur_posn.next
            fast_posn = fast_posn.next

        if n == 1:
            cur_posn.next = None
        else:
            cur_posn.next = cur_posn.next.next

        return head


head = ListNode(1)
cur_node = head

for x in range(4):
    cur_node.next = ListNode(x + 2)
    cur_node = cur_node.next

test = Solution()
print(test.removeNthFromEnd(head, 2))
