# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/16 20:05
@Author  : daluzi
@File    : 14-1.py
'''
# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
# 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

# 当所有绳段长度相等时，乘积最大；
# 最优的绳段长度为3


class Solution:
    def cuttingRope(self, n: int) -> int:
        # 动态规划

        # dp = [0] * (n + 1)
        # dp[2] = 1
        # for i in range (3, n + 1):
        #     for j in range(2, i):
        #         dp[i] = max(dp[i], max(j * (i - j), j * dp[i -j]))
        # return dp[n]

        # 贪心

        # if n < 4:
        #     return n - 1
        # res = 1
        # while n > 4:
        #     res *= 3
        #     n -= 3
        # return res * n

        # 数学推导

        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)