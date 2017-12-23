#!/usr/bin/env python
# -*- coding: utf-8 -*-

# I have use two methods to solve this problem

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # res = ''
        # step = max( (numRows - 1) * 2, 1 )
        # for line in range( min(numRows, len(s)) ):
        #     if line == 0 or line == numRows - 1:
        #         step1 = step2 = step
        #     else:
        #         step1 = step - 2 * line
        #         step2 = step - step1
        #
        #     j = line
        #     while j < len(s):
        #         res += s[j]
        #         j += step1
        #         step1, step2 = step2, step1
        # return res

        table = [[] for i in range(numRows)]
        line = 0
        up = True
        for i in s:
            table[line].append(i)
            if up:
                if line < numRows -1:
                    line += 1
                else:
                    line -= 1
                    up = False
            else:
                if line > 0:
                    line -= 1
                else:
                    line += 1
                    up = True

        res = ''
        for row in table:
            for col in row:
                res += col
        return res
