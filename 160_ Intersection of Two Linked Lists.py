
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        A= {} 
        while headA:
            A[headA.val] = True
            headA = headA.next
        while headB:
            if headB.val in A:
                return headB
            headB = headB.next
        return None
        
        
