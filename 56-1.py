# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 18:38
@Author  : daluzi
@File    : 56-1.py
'''

# 剑指 Offer 56 - I. 数组中数字出现的次数
# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

def singleNumber(nums):
    x = 0
    for num in nums:
        x ^= num
    return x
print(singleNumber([1,1,2,3,2]))


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in nums:         # 1. 遍历异或
            n ^= num
            print("n", n)
        while n & m == 0:        # 2. 循环左移，计算 m
            m <<= 1
        print(m)
        for num in nums:         # 3. 遍历 nums 分组
            if num & m:
                x ^= num # 4. 当 num & m != 0
                print("x", x)
            else:
                y ^= num
                print("y", y)      # 4. 当 num & m == 0
        return x, y              # 5. 返回出现一次的数字
