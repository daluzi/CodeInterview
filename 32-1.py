# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/3 19:48
@Author  : daluzi
@File    : 32-1.py
'''


# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
#
#  
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：
#
# [3,9,20,15,7]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return res