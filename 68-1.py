# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/29 21:24
@Author  : daluzi
@File    : 68-1.py
'''

# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # if not root: return None
        # def helper(node):
        #     if node.val == p.val:
        #         return p
        #     if node.val == q.val:
        #         return q
        #     if (node.val > p.val and node.val < q.val) or (node.val < p.val and node.val > q.val):
        #         return node
        #     elif node.val <= p.val and node.val <= q.val and node.left:
        #         return helper(node.right)
        #     elif node.val >= p.val and node.val >= q.val and node.right:
        #         return helper(node.left)
        #     else:
        #         return None

        # return helper(root)

        # while root:
        #     if root.val < p.val and root.val < q.val:
        #         root = root.right
        #     elif root.val > p.val and root.val > q.val:
        #         root = root.left
        #     else: break
        # return root

        # if p.val > q.val: p, q = q, p
        # while root:
        #     if root.val < p.val:
        #         root = root.right
        #     elif root.val > q.val:
        #         root = root.left
        #     else: break
        # return root

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root