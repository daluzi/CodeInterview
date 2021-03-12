# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/11 19:58
@Author  : daluzi
@File    : 07.py
'''

# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}

        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            preorder_root = preorder_left
            inorder_root = inorder.index(preorder[preorder_root])

            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root - inorder_left
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)

            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        return myBuildTree(0, n - 1, 0, n - 1)