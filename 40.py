# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/29 17:56
@Author  : daluzi
@File    : 40.py
'''
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
# 剑指 Offer 40. 最小的k个数
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # a = sorted(arr)
        # return a[:k]

        # 采用堆的方式，即python的heapq.heapify库
        if k == 0:
            return []

        hp = [-x for x in arr[:k]] #heapify是按照小顶堆构建的
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans