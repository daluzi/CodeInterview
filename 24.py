# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/1 21:51
@Author  : daluzi
@File    : 24.py
'''

# 剑指 Offer 24. 反转链表
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

# 迭代

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        currentNode, preNode = head, None
        while currentNode:
            temp = currentNode.next
            currentNode.next = preNode
            preNode = currentNode
            currentNode = temp

        return preNode

# 递归

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
