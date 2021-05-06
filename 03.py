# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/5 9:21
@Author  : daluzi
@File    : 03.py
'''


# 找出数组中重复的数字。
#
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 示例 1：
#
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # for x in nums:
        #     while nums.count(x)>1:
        #         return x


        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]

        for idx,i in enumerate(nums):
            while i != idx:
                if i == nums[i]: return i
                temp = nums[i]
                nums[i] = i
                nums[idx] = temp

        return None

        # i = 0
        # while i < len(nums):
        #     if nums[i] == i:
        #         i += 1
        #         continue
        #     if nums[i] == nums[nums[i]]: return nums[i]
        #     nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        # return -1


        # dic = set()
        # for num in nums:
        #     if num in dic: return num
        #     dic.add(num)
        # return -1