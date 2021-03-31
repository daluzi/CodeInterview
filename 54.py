# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 15:13
@Author  : daluzi
@File    : 54.py
'''
#
# 剑指 Offer 54. 二叉搜索树的第k大节点
# 给定一棵二叉搜索树，请找出其中第k大的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []

        def in_order(node):
            if node == None: return
            if node.right: in_order(node.right)
            res.append(node.val)
            if node.left: in_order(node.left)

        in_order(root)

        # a = res[::-1]
        return res[k - 1]