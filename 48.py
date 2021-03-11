# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/10 21:09
@Author  : daluzi
@File    : 48.py
'''

# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head, tail, res = 0, 0, 1
        if len(s) < 2: return len(s)
        while head < len(s) - 1:
            head += 1
            if s[head] not in s[tail:head]:
                res = max(res, head - tail + 1)
            else:
                while s[head] in s[tail:head]:
                    tail += 1
        return res