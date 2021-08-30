from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        first_num = queue.popleft() # 1
        cnt = 0
        for q in queue: # 2,3,2,3
            cnt += 1 # 일단 먼저 카운트가 들어간다
            if first_num > q: # [2,3,2,3]이 1과 비교됨
                break # 값이 내려갔으니 더이상 for문을 돌 필요가 없다
        answer.append(cnt)
    return answer