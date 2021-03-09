# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/9 9:01
@Author  : daluzi
@File    : 39.py
'''
#
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
#
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例
# 1:
#
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        return nums[int(length / 2)]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x
