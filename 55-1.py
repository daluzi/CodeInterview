# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 17:23
@Author  : daluzi
@File    : 55-1.py
'''

# 剑指 Offer 55 - I. 二叉树的深度
# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if not root: return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for n in queue:
                if n.left: tmp.append(n.left)
                if n.right: tmp.append(n.right)
            queue = tmp
            res += 1
        return res