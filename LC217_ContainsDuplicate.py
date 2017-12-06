#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def containsDuplicate(self, nums):
        """
        type nums: List[int]
        rtype: bool
        """

        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums):
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False
