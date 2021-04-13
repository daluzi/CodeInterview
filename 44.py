# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/12 21:33
@Author  : daluzi
@File    : 44.py
'''

# 剑指 Offer 44. 数字序列中某一位的数字
# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

# 请写一个函数，求任意第n位对应的数字。

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit
        return int(str(num)[(n-1) % digit])