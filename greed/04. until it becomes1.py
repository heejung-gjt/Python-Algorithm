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

# 범위가 클 경우 (시간복잡도 : log)

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k # n을 k로 나눌때 나누어떨어지지 않는 경우 k로 나누어 떨어지는 가장 가까운 수 n이 나오게 됨
    result += (n - target) # 1을 빼는 연산의 개수를 한번에 해준다.
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)








