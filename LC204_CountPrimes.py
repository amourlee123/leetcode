#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def countPrime(self, n):
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False

        x = 2
        while x * x < n:
            if isPrime[x]:
                p = x * x
                while p < n:
                    isPrime[p] = False
                    p += x

            x += 1

        return sum(isPrime)


