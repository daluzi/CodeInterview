# -*- coding: utf-8 -*-
'''
@Time    : 2021/5/6 19:59
@Author  : daluzi
@File    : leetcode_79.py
'''

# 79. 单词搜索
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        len_w = len(word)
        tmp = [[0] * n for _ in range(m)]  #创建的方式

        def recur(i, j, k):
            if k == len_w: return True
            if i < 0 or i >= m or j < 0 or j >= n: return False
            if board[i][j] != word[k] or tmp[i][j] != 0: return False

            tmp[i][j] = 1
            a = recur(i + 1, j, k + 1) or recur(i, j + 1, k + 1) or recur(i - 1, j, k + 1) or recur(i, j - 1, k + 1)
            tmp[i][j] = 0

            return a

        for i in range(m):
            for j in range(n):
                if recur(i, j, 0):
                    return True

        return False
