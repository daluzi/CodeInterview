# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/29 18:07
@Author  : daluzi
@File    : input_output.py
'''
from click._compat import raw_input

'''Python的输入是野生字符串，所以要自己转类型 
strip去掉左右两端的空白符，返回str 
slipt把字符串按空白符拆开，返回[str] 
map把list里面的值映射到指定类型，返回[type] 
 
EOF用抓异常 
 
print后面加逗号就不会换行，否则反之，当然3.x君自行传参 
'''

while True:
    try:
        a, b = map(int, raw_input().strip().split())
        print(a + b)
    except EOFError:
        break