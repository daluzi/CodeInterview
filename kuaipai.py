# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/29 17:33
@Author  : daluzi
@File    : kuaipai.py
'''

arr = [2, 4, 1, 0, 3, 5]
l, r = 0, len(arr) - 1


def quick_sort(arr, l, r):
    if l >= r: return
    i, j = l, r
    while i < j:
        while i < j and arr[j] >= arr[l]: j -= 1
        while i < j and arr[i] <= arr[l]: i += 1
        arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[i] = arr[i], arr[l]
    quick_sort(arr, l, i - 1)
    quick_sort(arr, i + 1, r)

quick_sort(arr, 0, r)
print(arr)