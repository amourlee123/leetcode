#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        type head: ListNode
        type val: int
        rtype: ListNode
        """

        ListNode cursor = head
        while( cursor != None ):
            if(head.val == val):
                head = head.next
                cursor = head
            elif(cursor.next != None && cursor.next.val == val):
                ListNode valNode = cursor.next
                cursor.next = valNode.next
                valNode.next = None
            else:
                cursor = cursor.next

        return head
