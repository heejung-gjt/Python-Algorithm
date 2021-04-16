'''
##문제 설명
리스트 L 과 정수 x 가 인자로 주어질 때, 리스트 내의 올바른 위치에 x 를 삽입하여 그 결과 리스트를 반환하는 함수 solution 을 완성하세요.
인자로 주어지는 리스트 L 은 정수 원소들로 이루어져 있으며 크기에 따라 (오름차순으로) 정렬되어 있다고 가정합니다.
예를 들어, L = [20, 37, 58, 72, 91] 이고 x = 65 인 경우, 올바른 리턴 값은 [20, 37, 58, 65, 72, 91] 입니다.
힌트: 순환문을 이용하여 올바른 위치를 결정하고 insert() 메서드를 이용하여 삽입하는 것이 한 가지 방법입니다.
주의: 리스트 내에 존재하는 모든 원소들보다 작거나 모든 원소들보다 큰 정수가 주어지는 경우에 대해서도 올바르게 처리해야 합니다.

## Pseudocode
- 오름차순되어있는 리스트들을 순환하면서 x보다 큰지 작은지 비교한다 , 순환문 이용한다
- 만약 리스트의 가장 마지막 요소가 x보다 작으면 x를 가장 마지막에 삽입해준다
- for문을 돌려 만약 L[i]의 값이 x보다 큰경우 i인덱스에 x를 삽입해준다
- 만약 L[i]의 값이 x보다 작은경우 continue처리를 해준다 
'''

#방법1
# def solution(L, x):
#   answer = []
#   if L[len(L)-1] < x:
#     L.insert(len(L),x)
#   else:
#     for i in range(len(L)):
#       if L[i] >= x:
#         L.insert(i,x)
#         break
#       else:
#         continue
#   answer = L
#   return answer
# answer = solution( [20, 37, 58, 72, 91], 65)
# print(answer)


#방법2
def solution(L, x):
  i = 0
  while x > L[i]:
    i += 1
    if i >= len(L):
      break
  L.insert(i,x)

  return L