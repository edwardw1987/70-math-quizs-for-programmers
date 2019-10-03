# -*- coding: utf-8 -*-
# 动态规划


def solve(m, n):
    m, n = m + 1, n + 1
    F = [[0] * n for _ in range(m)]
    F[0][0] = 1
    for i in range(m):
        for j in range(n):
             # 把男女人数相等的情况先排除掉
            if i != j and m - i != n - j:
                if j > 0:
                    F[i][j] += F[i][j - 1]
                if i > 0:
                    F[i][j] += F[i - 1][j]
    return F[m - 1][n - 2] + F[m - 2][n - 1]


print(solve(20, 10))
