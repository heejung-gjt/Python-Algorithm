
### Level1



#### 문제1번 
```
문자열 s의 길이가 4혹은 6이고, 
숫자로만 구성되있는지 확인해주는 함수, solution을 완성해라.
```

#### pseudocode
1. 문자열 길이가 4또는 6이 아니면 false 출력 (조건문 사용)   
2. isdigit()를 이용해 문자열에 숫자를 제외한 값이 들어왔는지 아닌지를 bool형으로 출력 (조건문 사용)   
3. 두개다 조건문 if문을 이용하기 때문에 삼항연산자를 사용       
 

#### ```코드```
```py
def solution(s):
  answer = True

  answer = True if(len(s) == 4 or len(s) == 6) and s.isdigit() == True else False

  return answer
```

#### ```리뷰 후 코드```
삼항 연산자를 쓰기에는 조건문이 너무 길어지므로 일반 if문을 쓰는 것이 ```가독성```면에서 좋다
```py
#1번
def solution(s):
  if len(s) == 4 or len(s) == 6 and s.isdigit():
    answer = True
  else:
    answer = False
  return answer
```

#### ```주의```

- or과 and문을 사용시 or의 조건문을 ```()``` 으로 묶어주어야 모든 테스트케이스를 통과할 수 있다. 항상 or의 조건문이 먼저 평가되어야 한다.

<br>


#### 문제2번 
```
길이가 같은 두 1차원 정수 배열a,b가 매개변수로 주어진다.
a와 b의 내적을 return하도록 solution함수를 완성해라 
```
#### ```pseudocode```
- 리스트 a와 b의 길이만큼 순차적으로 각각의 값만큼 더해준다        
- while문을 이용해 a,b의 인덱스 0 ~ n-1 에 존재하는 값들을 각각 곱해준후 answer에 누적으로 더한다    
- 인덱스 값 i가 len(a)또는 len(b)와 같아지면 반복문을 종료한다                


#### ```코드```
```py
def solution(a,b):
  answer = 0
  i = 0
  while True:
    if i == len(a):
      break
    answer += a[i] * b[i]
    i += 1
  return answer
```
#### ```리뷰 후 코드```
while문보다는 for문을 사용하는 것이 가독성면에서 더 좋다
```py
def solution(a,b):
  answer = 0
  for i in range(len(a)):
      answer += a[i] * b[i]
  return answer
```
zip을 이용해서 문제를 해결이 가능하다
```py
#2번
def solution(a,b):
  answer = 0
  for x, y in zip(a,b):
    answer += x * y
  return answer
```

#### ```질문```

- answer의 기본값이 ```answer=1234567890```으로 되어 있었지만 answer = 0으로 고친 후 문제를 풀었다. 기본값을 바꾸어도 괜찮은가?

<br>

<img src="https://user-images.githubusercontent.com/64240637/114377191-57440100-9bc1-11eb-8555-9343a09fefc4.png" width=400px height=200>
