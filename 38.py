# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/29 16:40
@Author  : daluzi
@File    : 38.py
'''

# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。


class Solution:
    def permutation(self, s: str) -> List[str]:
        # 递归的思想，做交换
        # c, res = list(s), []
        # def dfs(x):
        #     if x == len(c) - 1:
        #         res.append(''.join(c))
        #         return
        #     dic = set()
        #     for i in range(x, len(c)):
        #         if c[i] in dic: continue
        #         dic.add(c[i])
        #         c[i], c[x] = c[x], c[i]
        #         dfs(x + 1)
        #         c[i], c[x] = c[x], c[i]
        # dfs(0)
        # return res

        # 字符串的全排列代码
        if not s: return
        s = list(sorted(s))
        res = []
        def helper(s, tmp):
            if not s: res.append(''.join(tmp))
            for i, char in enumerate(s):
                if i > 0 and s[i] == s[i - 1]:
                    continue
                helper(s[:i]+s[i+1:], tmp+[char])
        helper(s, [])
        return res


# 数组的全排列
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def helper(nums,temp):
            if not nums:
                res.append(temp)
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                helper(nums[:i]+nums[i+1:],temp+[nums[i]])
        helper(nums,[])
        return res