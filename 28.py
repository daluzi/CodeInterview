# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/23 22:04
@Author  : daluzi
@File    : 28.py
'''

# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def helper(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val: return False
            return helper(L.left, R.right) and helper(L.right, R.left)

        return helper(root.left, root.right) if root else True
