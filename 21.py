# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/18 15:40
@Author  : daluzi
@File    : 21.py
'''
# 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while nums[left] % 2 == 1 and left < right:
                left += 1
            while nums[right] % 2 == 0 and right > left:
                right -= 1
            cur = nums[left]
            nums[left] = nums[right]
            nums[right] = cur
            left += 1
            right -= 1
        return nums