# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = self
        start.next = head
        while start.next and start.next.next:
            temp_1 = start.next
            temp_2 = temp_1.next
            start.next, temp_2.next, temp_1.next = temp_2, temp_1, temp_2.next
            start = temp_1

        return self.next


test_head = ListNode(1)
cur_node = test_head

for x in range(4):
    cur_node.next = ListNode(x + 2)
    cur_node = cur_node.next

test = Solution()
out = test.swapPairs(test_head)
print(out)
