# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        p1 = dummy
        p2 = dummy
        for i in range (n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
        ##双指针解法：使用两个指针，第一个指针从链表的第n + 1个节点前进，而第二个指针从列表的开始处前进。这样两个指针相距n个节点，两个指针一块前进，这样当第一个指针到达最后一个节点时，第二个指针指向倒数第n+1个节点，接下来就可以直接移除倒数第n个节点了。时间复杂度O(L)，空间复杂度O(1)
