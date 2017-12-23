#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        y = '%d' % x
        return x == int(y[::-1])
