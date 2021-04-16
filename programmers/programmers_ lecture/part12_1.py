'''
코드 구현 참고
스택의 맨 위에 있는 연산자와의 우선순위를 비교하여 같거나 높은 우선순위를 pop하여 출력한다
이때 맨 위의 연산자를 꺼내지 않고 단순히 비교하기 위해 peek라는 함수를 사용한다

스택에 남아 있는 연산자 모두 pop()하는 순환문 
while not opStack.isEmpty(): 
'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    return answer