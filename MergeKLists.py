# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        valid_lists = []
        for list in lists:
            if list:
                valid_lists.append(list)

        list_num = len(valid_lists)

        if list_num == 0:
            return []

        def sort_lists(sort_list):
            return sort_list.val

        valid_lists.sort(key=lambda sort_list: sort_list.val)

        i = 1
        l1 = valid_lists[i - 1]
        merged_list = l1

        while i < list_num:
            l2 = valid_lists[i]

            cur_node = l1
            next_node = l2
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

            l1 = merged_list
            i += 1

        return merged_list

head1 = ListNode(1)
# node = head1
# node.next = ListNode(5)
headtest = ListNode(0)

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

head3 = ListNode(0)
node3 = head3
node3.next = ListNode(2)
node3 = node3.next
node3.next = ListNode(4)
node3 = node3.next
node3.next = ListNode(10)
node3 = node3.next

list_arr = [head1, head2, head3]

test = Solution()
print(test.mergeKLists([head1, headtest]))
