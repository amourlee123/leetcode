#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def isHappy(self, n):
        """
        type n: int
        rtype: bool
        """
        slow = self.getSquareSum(n)
        fast = self.getSquareSum(n)
        fast = self.getSquareSum(fast)
        while(slow != fast):
            slow = self.getSquareSum(slow)
            fast = self.getSquareSum(fast)
            fast = self.getSquareSum(fast)
        if( slow == 1 ):
            return True
        else:
            return False

    def getSquareSum(self, n):
        sum = 0
        while(n):
            tmp = n % 10
            sum += tmp*tmp
            n = n // 10

        return sum
