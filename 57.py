# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/31 10:17
@Author  : daluzi
@File    : 57.py
'''

# 剑指 Offer 57. 和为s的两个数字
#
# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [i for i in nums if i <= target]
        left, right = 0, len(new_nums) - 1
        while left <= right:
            if new_nums[left] + new_nums[right] == target:
                return [new_nums[left], new_nums[right]]
            elif new_nums[left] + new_nums[right] < target:
                left += 1
            elif new_nums[left] + new_nums[right] > target:
                right -= 1
