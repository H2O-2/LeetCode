# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        lastElement = None
        ptr = head
        cur = None
        prev = None
        for _ in range(k):
            if ptr is None:
                return head
            cur = ListNode(ptr.val)

            if prev:
                cur.next = prev
            else:
                lastElement = cur

            prev = cur

            ptr = ptr.next

        lastElement.next = self.reverseKGroup(ptr, k)
        return cur


test = ListNode(1)
testptr = test
for i in range(4):
    testptr.next = ListNode(i + 2)
    testptr = testptr.next

sol = Solution()
answer = sol.reverseKGroup(test, 2)

while answer is not None:
    print(answer.val)
    answer = answer.next
