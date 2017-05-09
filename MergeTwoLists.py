# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        cur_node = l1 if (l1.val <= l2.val) else l2
        next_node = l1 if (l1.val > l2.val) else l2
        merged_list = ListNode(cur_node.val)
        cur_posn = merged_list

        while True:
            if cur_node.next is None:
                break

            if cur_node.next.val <= next_node.val:
                cur_node = cur_node.next
            else:
                temp = cur_node.next
                cur_node = next_node
                next_node = temp

            cur_posn.next = ListNode(cur_node.val)
            cur_posn = cur_posn.next

        cur_posn.next = next_node

        return merged_list


head1 = ListNode(1)
node = head1
node.next = ListNode(5)

head2 = ListNode(2)
node = head2

node.next = ListNode(3)
node = node.next

node.next = ListNode(6)
node = node.next

node.next = ListNode(7)
node = node.next

node.next = ListNode(8)
node = node.next

test = Solution()
print(test.mergeTwoLists(head1, head2))
