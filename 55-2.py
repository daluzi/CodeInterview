# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 17:22
@Author  : daluzi
@File    : 55-2.py
'''

# 剑指 Offer 55 - II. 平衡二叉树
# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

        # def recur(root):
        #     if not root: return 0
        #     left = recur(root.left)
        #     if left == -1: return -1
        #     right = recur(root.right)
        #     if right == -1: return -1
        #     return max(left, right) + 1 if abs(left - right) <= 1 else -1
        # return recur(root) != -1