# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/31 9:42
@Author  : daluzi
@File    : 56-2.py
'''

# 剑指 Offer 56 - II. 数组中数字出现的次数 II
#
# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        for key, value in h.items():
            if value == 1:
                return key