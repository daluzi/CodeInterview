# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/1 19:33
@Author  : daluzi
@File    : 06.py
'''

# 剑指 Offer 06. 从尾到头打印链表
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 递归
        # return self.reversePrint(head.next) + [head.val] if head else []

        # 辅助栈
        auxiliaryArray = []

        while head:
            auxiliaryArray.append(head.val)
            head = head.next

        return auxiliaryArray[::-1]