# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/29 14:49
@Author  : daluzi
@File    : 36.py
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def dfs(cur):
            if not cur: return
            dfs(cur.left)

            if not self.pre:
                self.head = cur
            else:
                self.pre.right, cur.left = cur, self.pre
            self.pre = cur

            dfs(cur.right)

        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head