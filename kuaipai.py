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
    print(arr)
    quick_sort(arr, l, i - 1)
    quick_sort(arr, i + 1, r)

quick_sort(arr, 0, r)
print(arr)



def quick_sort_2(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] #找到一个基准值
        # 遍历整个列表，将小于这个基准值的元素放到一个子列表中
        less = [i for i in array[1:] if i < pivot]
        # 遍历整个列表，将大于这个基准值的元素放到一个子列表中
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort_2(less) + [pivot] + quick_sort_2(greater)

print(quick_sort_2([2, 4, 1, 0, 3, 5]))
