# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 14:53
@Author  : daluzi
@File    : 53-2.py
'''

# 剑指 Offer 53 - II. 0～n-1中缺失的数字
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # a = sorted(nums)
        # for index, i in enumerate(a):
        #     if index != i:
        #         return index
        # return len(nums)

        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == mid:
                i = mid + 1
            else:
                j = mid - 1
        return i