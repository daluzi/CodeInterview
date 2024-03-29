# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/29 11:00
@Author  : daluzi
@File    : 35.py
'''


# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # DFS
        # def dfs(head):
        #     if not head: return None
        #     if head in visited:
        #         return visited[head]
        #     copy = Node(x = head.val, next = None, random = None)
        #     visited[head] = copy
        #     copy.next = dfs(head.next)
        #     copy.random = dfs(head.random)
        #     return copy

        # visited = {}

        # return dfs(head)

        # # BFS
        # def bfs(head):
        #     clone = Node(head.val, None, None)
        #     queue = [head]
        #     visited[head] = clone
        #     while queue:
        #         tmp = queue.pop()
        #         if tmp.next and tmp.next not in visited:
        #             visited[tmp.next] = Node(tmp.next.val, [], [])
        #             queue.append(tmp.next)
        #         if tmp.random and tmp.random not in visited:
        #             visited[tmp.random] = Node(tmp.random.val, [], [])
        #             queue.append(tmp.random)
        #         visited[tmp].next = visited.get(tmp.next)
        #         visited[tmp].random = visited.get(tmp.random)
        #     # print(visited == clone)
        #     return clone
        # visited = {}
        # return head if not head else bfs(head)

        # # 迭代
        # def getClonedNode(node):
        #     if node:
        #         if node in visited:
        #             return visited[node]
        #         else:
        #             visited[node] = Node(node.val, None, None)
        #             return visited[node]
        #     return None
        # visited = {}
        # if not head: return head
        # old_node = head
        # new_node = Node(old_node.val, None, None)
        # visited[old_node] = new_node
        # while old_node:
        #     new_node.next = getClonedNode(old_node.next)
        #     new_node.random = getClonedNode(old_node.random)
        #     old_node = old_node.next
        #     new_node = new_node.next
        # return visited[head]

        # 改进版迭代
        if not head: return head
        cur = head
        while cur:
            new_node = Node(cur.val, None, None)  # 克隆新结点
            new_node.next = cur.next
            cur.next = new_node  # 克隆新结点在cur 后面
            cur = new_node.next  # 移动到下一个要克隆的点
        cur = head

        while cur:  # 链接random
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur_old_list = head  # 将两个链表分开
        cur_new_list = head.next
        new_head = head.next
        while cur_old_list:
            cur_old_list.next = cur_old_list.next.next
            cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
            cur_old_list = cur_old_list.next
            cur_new_list = cur_new_list.next
        return new_head