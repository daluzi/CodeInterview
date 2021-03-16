# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/11 22:00
@Author  : daluzi
@File    : 10-1.py
'''
# 斐波那契数列
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

class Solution:
    def fib(self, n: int) -> int:
        a = [0, 1]
        for i in range(2,n+1):
            a.append((a[i-1] + a[i -2]) % 1000000007)
        return a[n]