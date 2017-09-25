# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ret = None
        tail = None
        p1 = l1
        p2 = l2
        while (p1 and p2):
            tmp = carry + p1.val + p2.val
            carry = 0
            if tmp >= 10:
                carry = 1

            newNode = ListNode(tmp % 10)
            if not ret:
                ret = newNode
                tail = ret
            else:
                tail.next = newNode
                tail = newNode

            p1 = p1.next 
            p2 = p2.next

        if p2:
            while p2:
                tmp = carry + p2.val
                carry = 0
                if tmp >= 10:
                    carry = 1
                newNode = ListNode(tmp % 10)
                tail.next = newNode
                tail = newNode
                
                p2 = p2.next
            
        elif p1:
            while p1:
                tmp = carry + p1.val
                carry = 0
                if tmp >= 10:
                    carry = 1
                newNode = ListNode(tmp % 10)
                tail.next = newNode
                tail = newNode
                
                p1 = p1.next

        
        if carry == 1:
            tail.next = ListNode(1)
            
        return ret
        
