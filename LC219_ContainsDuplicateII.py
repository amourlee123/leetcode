#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # type nums: List[int]
    # type k: int
    # rtype: bool

    def containsNearbyDuplicate(self, nums, k):
        numDict = dict()
        for x in range(len(nums)):
            if numDict.get(nums[x]) != None:
                idx = numDict.get(nums[x])
                if idx > 0 and x - idx <= k:
                    return True
            dict[nums[x]]= x
        return False
