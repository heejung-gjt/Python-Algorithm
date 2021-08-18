# -*- coding: utf-8 -*-

"""
date: 0813
source: 2019 국가 교육기관 코딩 테스트
solution time: 30min
"""

n, m = map(int , input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

# 2중 반복문 구조 사용
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    
    min_value = 1000
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

