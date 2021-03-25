# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/25 19:26
@Author  : daluzi
@File    : 32-2.py
'''
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        a = []
        n = [root]
        while n:
            res = []
            for _ in range(len(n)):
                node = n.pop(0)
                res.append(node.val)
                if node.left: n.append(node.left)
                if node.right: n.append(node.right)
            a.append(res)
        return a