'''
##문제 설명
메서드 traverse() 는 리스트를 리턴하되, 
이 리스트에는 연결 리스트의 노드들에 들어 있는 데이터 아이템들을 연결 리스트에서의 순서와 같도록 포함합니다. 
예를 들어, LinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면,
올바른 리턴 값은 [43, 85, 62] 입니다.
'''

class Node:
  def __init__(self,item):
    self.data = item
    self.next = None

class LinkedList:
  def __init__(self):
    self.nodeCount = 0
    self.head = None
    self.tail = None
  
  def getAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
      return None
    i = 1
    curr = self.head
    while i < pos:
      curr = curr.next
      i += 1
    return curr

  def traverse(self):
    curr = self.head
    answer = []
    while curr != None:
      answer.append(curr.data)
      curr = curr.next
    return answer

def solution(x):
  return 0
