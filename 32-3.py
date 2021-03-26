# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/25 19:25
@Author  : daluzi
@File    : 32-3.py
'''

# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        level = 1
        a = []
        res = [root]
        while res:
            temp = []
            for _ in range(len(res)):
                node = res.pop(0)
                if level % 2 == 1:
                    temp.append(node.val)
                elif level % 2 == 0:
                    temp.insert(0, node.val)
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
            level += 1
            a.append(temp)
        return a