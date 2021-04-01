# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/31 14:06
@Author  : daluzi
@File    : 58-1.py
'''


# 剑指 Offer 58 - I. 翻转单词顺序
# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        # res = s.split()[::-1]
        # result = ' '.join(res)
        # return result

        # return ' '.join(s.strip().split()[::-1])

        s = s.strip()
        res = []
        i, j = len(s) - 1, len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] != " ": i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == ' ': i -= 1
            j = i
        return ' '.join(res)