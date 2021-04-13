# -*- coding: utf-8 -*-
'''
@Time    : 2021/4/12 20:44
@Author  : daluzi
@File    : 34.py
'''

# 剑指 Offer 34. 二叉树中和为某一值的路径
# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                # print(path)
                res.append(list(path))
                # print(res)
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()
        recur(root, target)
        return res