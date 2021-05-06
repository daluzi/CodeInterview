# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/2 21:18
@Author  : daluzi
@File    : 18.py
'''


#
# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
#
# 返回删除后的链表的头节点。
#
# 注意：此题对比原题有改动
#
# 示例 1:
#
# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
# 示例 2:
#
# 输入: head = [4,5,1,9], val = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # cur, dum = head, ListNode(0)
        # if head.val == val:
        #     head = head.next
        #     return head
        # while cur:
        #     if cur.val == val:
        #         dum.next = cur.next
        #         cur = dum
        #     dum = cur
        #     cur = cur.next
        # return head

        p = ListNode(-1)
        p.next = head
        q = p
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                break
            p = p.next
        return q.next