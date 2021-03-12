# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/11 21:30
@Author  : daluzi
@File    : 09.py
'''

# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

class CQueue:

    def __init__(self):
        self.que, self.a = [], []

    def appendTail(self, value: int) -> None:
        self.que.append(value)

    def deleteHead(self) -> int:
        if self.a: return self.a.pop()
        if not self.que: return -1
        self.a = self.que[::-1]
        self.que = []
        return self.a.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()