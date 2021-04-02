# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/31 14:42
@Author  : daluzi
@File    : 59-1.py
'''

# 剑指 Offer 59 - I. 滑动窗口的最大值

# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k > n : return 0
        if nums == []: return []

        res = []
        i = 0
        while i <= n - k:
            j = i + k - 1
            res.append(max(nums[i: j + 1]))
            i += 1
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res
