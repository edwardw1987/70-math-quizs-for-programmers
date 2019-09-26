# -*- coding: utf-8 -*-
from collections import defaultdict

country = ["Brazil", "Croatia", "Mexico", "Cameroon",
           "Spain", "Netherlands", "Chile", "Australia",
           "Colombia", "Greece", "Cote d'Ivoire", "Japan",
           "Uruguay", "Costa Rica", "England", "Italy",
           "Switzerland", "Ecuador", "France", "Honduras",
           "Argentina", "Bosnia and Herzegovina", "Iran",
           "Nigeria", "Germany", "Portugal", "Ghana",
           "USA", "Belgium", "Algeria", "Russia",
           "Korea Republic"]
# 用于检查该国名是否使用过的标记数组
# 解法一回溯
global res, string
res, string = 0, []


def search(prev, depth, country, s):
    flag = False
    for i, c in enumerate(country):
        if c and c[0] == prev[-1].upper():
            flag = True
            temp = country[i]
            country[i] = ''
            search(c, depth + 1, country, s + "->" + c)
            country[i] = temp
    if not flag:
        global res, string
        if depth > res:
            res = depth
            string = [s]
        elif depth == res:
            string.append(s)


for i, c in enumerate(country):
    temp = country[i]
    country[i] = ''
    search(c, 1, country, c)
    country[i] = temp
print(res)
print('\n'.join(string))
