#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        val, start, end = 0, 0, 0
        countDict = {}
        for c in s:
            end += 1
            countDict[c] = countDict.get(c, 0) + 1
            while countDict[c] > 1:
                countDict[s[start]] -= 1
                start += 1
            val = max(val, end - start)
        return val
