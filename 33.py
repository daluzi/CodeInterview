# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/3 21:27
@Author  : daluzi
@File    : 33.py
'''

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
#
#  
#
# 参考以下这颗二叉搜索树：
#
#      5
#     / \
#    2   6
#   / \
#  1   3
# 示例 1：
#
# 输入: [1,6,3,2,5]
# 输出: false
# 示例 2：
#
# 输入: [1,3,2,6,5]
# 输出: true

# class Solution:
#     def verifyPostorder(self, postorder: List[int]) -> bool:
#         length = len(postorder)
#         if length > 3:
#             return self.verifyPostorder(postorder[:int(2/length)]) or self.verifyPostorder(postorder[int(2/length):])
#         if length == 3:
#             if postorder[0] <= postorder[1] <= postorder[2]:
#                 return True
#             else:
#                 return False
#         if length == 2:
#             return bool(postorder[0] <= postorder[1])

class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)