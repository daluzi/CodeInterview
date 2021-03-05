# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/1 21:51
@Author  : daluzi
@File    : 24.py
'''


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        currentNode, preNode = head, None
        while currentNode:
            temp = currentNode.next
            currentNode.next = preNode
            preNode = currentNode
            currentNode = temp

        return preNode