#2번
def solution(a,b):
  answer = 0
  i = 0

  while True:
    if i == len(a):
      break
    answer += a[i] * b[i]
    i += 1
  
  return answer