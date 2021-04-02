# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/31 19:45
@Author  : daluzi
@File    : huawei-test1.py
'''

import sys
inp = {}
for line in sys.stdin:
    lines = list(line.strip().split(" "))
    if lines[0] == "":
        break
    teams, cores = "".join(list(lines[0].split("-"))), "".join(list(lines[1].split(":")))
    inp[teams] = cores
result = {}
for key, value in enumerate(inp):
    if int(inp[value][0]) > int(inp[value][1]):
        if value[0] in result: result[value[0]] += 3
        else: result[value[0]] = 3
        if value[1] not in result: result[value[1]] = 0
    elif int(inp[value][0]) == int(inp[value][1]):
        if value[0] in result: result[value[0]] += 1
        else: result[value[0]] = 1
        if value[1] in result:
            result[value[1]] += 1
        else:
            result[value[1]] = 1
    elif int(inp[value][0]) < int(inp[value][1]):
        if value[0] in result: result[value[0]] += 0
        else: result[value[0]] = 0
        if value[1] in result:
            result[value[1]] += 3
        else:
            result[value[1]] = 3
result = sorted(result.items(), key=lambda x:x[1], reverse=False)
s = []
for key, value in enumerate(result):
    s.append(str(value[0]) + " " + str(value[1]))
print(",".join(s))
