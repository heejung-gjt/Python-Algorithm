'''
stack/queue 활용 문제
기능개발
'''

def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i] # 동시에 계속 더해진다.
        
        while progresses[0] >= 100: # 첫번째 인덱스값이 0인 경우에 / 이미 동시에 시작했기 때문에 100이 이미 된 요소들이 cnt +=1 을 연속으로 진행
            progresses.pop(0) # pop 해준다
            speeds.pop(0)
            cnt += 1 
            
            if not progresses: # 만약 progresses가 없다면 break
                break
        
        if cnt > 0: 
            answer.append(cnt)
    
    return answer