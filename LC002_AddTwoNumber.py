#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# define for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        L = result
        carry = 0
        while l1 or l2 or carry:
            global carry
            sum = carry
            carry = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum = sum % 10
            L.next = ListNode(sum)
            L = L.next
        return result.next
            
            
