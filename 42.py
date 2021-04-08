# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/8 15:59
@Author  : daluzi
@File    : 42.py
'''

# 剑指 Offer 42. 连续子数组的最大和
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)