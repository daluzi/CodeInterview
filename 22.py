# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/1 20:46
@Author  : daluzi
@File    : 22.py
'''

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter