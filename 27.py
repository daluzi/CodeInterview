# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/18 15:50
@Author  : daluzi
@File    : 27.py
'''

# 剑指 Offer 27. 二叉树的镜像
# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root