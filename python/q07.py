# -*- coding: utf-8 -*-
'''
日期的二进制转换
问题:
把年月日表示为 YYYYMMDD 这样的 8 位整数， 
然后把这个整数转换成 二进制数并且逆序排列，
再把得到的二进制数转换成十进制数，求与原日期一 致的日期。 
求得的日期要在上一次东京奥运会（1964 年 10 月 10 日）
到下一 次东京奥运会（预定举办日期为 2020 年 7 月 24 日）之间。
'''

DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def solve(startdate, enddate):
    res = []
    for date in range(startdate, enddate + 1):
        bdate = bin(date)[2:]
        bdater = bdate[::-1]
        if bdate == bdater:  # 检查是否是回文串
            s = str(date)
            y, m, d = int(s[:4]), int(s[4:6]), int(s[6:])
            if 1 <= m <= 12:
                dlimit = DAYS[m - 1]
                if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                    if m == 2:
                        dlimit += 1
                if 1 <= d <= dlimit:
                    res.append(date)
    return res


print(solve(19641010, 20200724))
