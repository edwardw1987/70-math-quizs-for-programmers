# -*- coding: utf-8 -*-


def solve(N):
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    visited[0][0] = 1

    def backtrack(N, x, y, n):
        if n == N:
            return 1
        res = 0
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                res += backtrack(N, nx, ny, n + 1)
                visited[nx][ny] = 0
        return res
    return backtrack(N, 0, 0, 0)


print(solve(3))
print(solve(12))
