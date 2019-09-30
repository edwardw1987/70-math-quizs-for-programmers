# -*- coding: utf-8 -*-
from collections import deque


def cutBar(m, n):
    res, now = 0, 1
    while now < n:
        now += now if now < m else m
        res += 1
    return res


def cutBarBFS(m, n):
    if n == 1:
        return 0
    que = deque([n])
    res = 0
    while que:
        size = len(que)
        for _ in range(min(m, size)):
            bar = que.popleft()
            left = bar >> 1
            right = bar - left
            if left > 1:
                que.append(left)
            if right > 1:
                que.append(right)
        res += 1
    return res


print cutBar(3, 8)
print cutBar(3, 20)
print cutBar(5, 100)
print cutBar(1, 1)
