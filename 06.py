# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/1 19:33
@Author  : daluzi
@File    : 06.py
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        auxiliaryArray = []

        while head:
            auxiliaryArray.append(head.val)
            head = head.next

        return auxiliaryArray[::-1]