'''
stack/queue 활용 문제
프린터
'''

# pop과 append 함수를 사용한다

def solution(priorities, location):
    
    priority_list = [(i, num) for i, num in enumerate(priorities)] # enumerate로 인덱스와 값을 튜플로 묶는다
    new_list = []
    
    while priority_list:
        index = priority_list.pop(0) #
        priority_num = index[1]
        p_list = [priority for index, priority in priority_list]
        if p_list:
            max_p = max(p_list)
        
        if priority_num >= max_p:
            new_list.append(index)
        else:
            priority_list.append(index)
    
    for i, item in enumerate(new_list):
        if item[0] == location:
            return i + 1
        
        
               
print(solution([1, 1, 9, 1, 1, 1],0))