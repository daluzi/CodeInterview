# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/18 16:44
@Author  : daluzi
@File    : 29.py
'''


# 剑指 Offer 29. 顺时针打印矩阵
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i])
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i])
            b -= 1
            if t > b: break
            for i in range(b ,t - 1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break

        return res
