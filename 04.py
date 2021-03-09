# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/8 20:38
@Author  : daluzi
@File    : 04.py
'''

# 在一个
# n * m
# 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
#
#
# 示例:
#
# 现有矩阵
# matrix
# 如下：
#
# [
#     [1, 4, 7, 11, 15],
#     [2, 5, 8, 12, 19],
#     [3, 6, 9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
# 给定
# target = 5，返回
# true。
#
# 给定
# target = 20，返回
# false。
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # for i in matrix:
        #     for j in i:
        #         if j == target: return True
        # return False

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        height = len(matrix)
        width = len(matrix[0])

        row = 0
        column = width - 1
        while row < height and column >= 0:
            if matrix[row][column] > target:
                column = column - 1
            elif matrix[row][column] < target:
                row = row + 1
            elif matrix[row][column] == target:
                return True
        return False