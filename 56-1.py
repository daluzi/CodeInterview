# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 18:38
@Author  : daluzi
@File    : 56-1.py
'''


def singleNumber(nums):
    x = 0
    for num in nums:
        x ^= num
    return x
print(singleNumber([1,1,2,3,2]))