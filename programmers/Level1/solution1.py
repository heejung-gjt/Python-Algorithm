#1번
def solution(s):
  answer = True
  
  answer = True if(len(s) == 4 or len(s) == 6) and s.isdigit() == True else False
  return answer