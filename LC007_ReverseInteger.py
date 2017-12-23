#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        num = 0
        s = x // abs(x)
        x = abs(x)
        while x > 9:
            c = x % 10
            x = x // 10
            num = num * 10 + c
        num = num * 10 + x
        if num > (2**31-1):
            return 0
        return num * s
