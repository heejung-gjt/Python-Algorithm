# -*- coding: utf-8 -*-

"""
date: 0812
source: 2019 국가 교육기관 코딩 테스트
solution time: 30min
"""


n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

first = num_list[-1]
second = num_list[-2]
cnt = 0

while True:
    for i in range(k):        
        if m == 0:
            break    
        cnt += first
        m -= 1
    if m == 0:
        break
    m -= 1
    cnt += second

print(cnt)


# 반복되는 수열에 대해서 파악, 가장 큰 수가 더해지는 횟수를 더해서 구하기
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

first = num_list[-1]
second = num_list[-2]

result = 0
first_cnt = (m // k + 1) * k + m % (k +1)
result += first_cnt * first
result += (m - first_cnt) * second

print(result)