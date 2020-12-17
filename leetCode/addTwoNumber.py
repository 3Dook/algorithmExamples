# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        temp = ListNode()
        rNode = temp
        
        while(l1 != None or l2 != None or carry != 0):
            if(l1 == None):
                l1_val = 0
            else:
                l1_val = l1.val
                
            if(l2 == None):
                l2_val = 0
            else: 
                l2_val = l2.val
            #l1_val = l1.val || 0
            #l2_val = l2.val || 0
            sum = l1_val + l2_val + carry

            carry = sum // 10
            sum = sum % 10
            # make the node
            temp.val = sum

            #iterate 
        
            if(l1 != None):
                l1 = l1.next
            if(l2 != None):
                l2 = l2.next
        
            if(l1 != None or l2 != None or carry != 0):
                temp.next = ListNode()
                temp = temp.next
            
        return rNode