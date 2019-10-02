# -*- coding: utf-8 -*-
# 考拉兹猜想(改)
def is_loop(n):
    check = n * 3 + 1
    while check != 1:
        check = check * 3 + 1 if check % 2 else check // 2
        if check == n:
            return True
    return False


res = 0
for i in range(2, 10001, 2):
    if is_loop(i):
        res += 1
print(res)
