# -*- coding: utf-8 -*-
class Solution(object):
    def change(self, target, coins, usable):
        def backtrack(target, coins, usable, p):
            if p == len(coins):
                return 1 if 0 <= usable and target == 0 else 0
            coin = coins[p]
            res = 0
            for i in range(target // coin + 1):
                res += backtrack(target - coin * i,
                                 coins, usable - i, p + 1)
            return res
        return backtrack(target, coins, usable, 0)


s = Solution()
print s.change(1000, [500, 100, 50, 10], 15)
