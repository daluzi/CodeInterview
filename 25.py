# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/2 19:21
@Author  : daluzi
@File    : 25.py
'''

# 剑指 Offer 25. 合并两个排序的链表

# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        former = latter = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                latter.next ,l1 = l1, l1.next
            else:
                latter.next, l2 = l2, l2.next
            latter = latter.next
        latter.next = l1 if l1 else l2
        return former.next