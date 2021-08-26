"""
해시 관련 문제
"""

def solution(participant, completion):
    answer = {}
    for i in participant:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1

    for i in completion:
        if i in answer:
            answer[i] -= 1

    return [k for k in answer.keys() if answer[k] > 0][0]