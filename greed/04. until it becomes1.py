# -*- coding: utf-8 -*-
"""
date: 0813
source: 2018 E기업 알고리즘 대회
solution time: 30min
"""

n, k = map(int, input().split())
cnt = 0

while True:
    if n == 1:
        break
    if n % k != 0:
        cnt += 1
        n -= 1
    if n % k == 0:
        cnt += 1
        n //= k

# 범위가 클 경우 
