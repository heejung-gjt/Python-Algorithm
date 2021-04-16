'''
## 문제 설명
리스트 L 은 정수들로 이루어져 있고 그 순서는 임의로 부여되어 있다고 가정하며,
동일한 원소가 반복하여 들어 있을 수 있습니다.
이 안에 정수 x 가 존재하면 그것들을 모두 발견하여 해당 인덱스들을 리스트로 만들어
반환하고, 만약 존재하지 않으면 하나의 원소로 이루어진 리스트 [-1] 를 반환하는 함수를 완성하세요.

## Pseudocode
- 오름차순되어있는 리스트들을 순환하면서 x보다 큰지 작은지 비교한다 , 순환문 이용한다
- 만약 리스트의 가장 마지막 요소가 x보다 작으면 x를 가장 마지막에 삽입해준다
- for문을 돌려 만약 L[i]의 값이 x보다 큰경우 i인덱스에 x를 삽입해준다
- 만약 L[i]의 값이 x보다 작은경우 continue처리를 해준다 
'''


def solution(L, x):
    answer = []
    if x not in L:
        return [-1]
    else:
        for i in range(len(L)):
            if L[i] == x:
                answer.append(i)
        return answer


test = [64, 72, 83, 72, 54]
print(solution(test, 72))

'''
def solution(L,x):
    answer = []
    if x in L:
        for i in range(len(L)):
            if L[i] == x:
                answer.append(i)
        return answer
    return [-1]
'''