# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/31 11:06
@Author  : daluzi
@File    : 57-2.py
'''

# 剑指 Offer 57 - II. 和为s的连续正数序列
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # left, right = 1, 2
        # result = []
        # while left < target:
        #     s, res = left, [left]
        #     right = left + 1
        #     while right < target:
        #         s += right
        #         if s < target:
        #             res.append(right)
        #         elif s == target:
        #             res.append(right)
        #             result.append(res)
        #         elif s > target:
        #             break
        #         right += 1
        #     left += 1

        # return result

        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res
