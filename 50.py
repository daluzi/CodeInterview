# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/12 19:48
@Author  : daluzi
@File    : 50.py
'''

# 剑指 Offer 50. 第一个只出现一次的字符
# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

class Solution:
    def firstUniqChar(self, s: str) -> str:
        std = {}
        for i in s:
            std[i] = not i in std
        for i in s:
            if std[i]: return i
        return ' '