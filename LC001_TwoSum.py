#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: List[int]
        """
        indexDict = {}
        for idx, num enumerate(nums):
            diff = target - num
            if diff in indexDict:
                return [indexDict[diff], idx]
            indexDict[num] = idx
