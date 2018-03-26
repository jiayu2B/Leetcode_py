# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        while head:
            arr.append(head)
            head = head.next
        arr.reverse()
        link = ListNode(0)
        p = link
        for i in range(0, len(arr)):
            p.next = arr[i]
            p = p.next
        p.next = None
        return link.next
