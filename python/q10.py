# -*- coding: utf-8 -*-
'''
轮盘的最大值
问题:
当 2 ≤ n ≤ 36 时，求连续 n 个数之和最大的情况，
并找出满足条件“欧式 规则下的和小于美式规则下的和”的 n 的个数。
'''
european = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8,
            23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
american = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13,
            1, 00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]


def solve():
    def sum_max(roulette, n):
        res = 0
        now = sum(roulette[:n])
        size = len(roulette)
        for i in range(size):
            now += roulette[(i + n) % size] - roulette[i]
            res = max(now, res)
        return res
    return sum(sum_max(european, i) < sum_max(american, i)for i in range(2, 37))


print(solve())
