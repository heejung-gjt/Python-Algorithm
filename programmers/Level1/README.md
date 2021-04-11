
### Level1

#### 문제1번 

#### pseudocode
1. 문자열 길이가 4또는 6이 아니면 false 출력 (조건문 사용)   
2. isdigit()를 이용해 문자열에 숫자를 제외한 값이 들어왔는지 아닌지를 bool형으로 출력 (조건문 사용)   
3. 두개다 조건문 if문을 이용하기 때문에 삼항연산자를 사용       

<img src="https://user-images.githubusercontent.com/64240637/114295395-f42e6d80-9adf-11eb-909a-c15140d2cde7.png" width=700px, height=500px>
 

#### ```코드```
```py
def solution(s):
  answer = True

  answer = True if(len(s) == 4 or len(s) == 6) and s.isdigit() == True else False

  return answer
```

#### ```주의```

- or과 and문을 사용시 or의 조건문을 ```()``` 으로 묶어주어야 모든 테스트케이스를 통과할 수 있다. 항상 or의 조건문이 먼저 평가되어야 한다.

<br>


#### 문제2번 

#### ```pseudocode```
- 리스트 a와 b의 길이만큼 순차적으로 각각의 값만큼 더해준다        
- while문을 이용해 a,b의 인덱스 0 ~ n-1 에 존재하는 값들을 각각 곱해준후 answer에 누적으로 더한다    
- 인덱스 값 i가 len(a)또는 len(b)와 같아지면 반복문을 종료한다                

<img src="https://user-images.githubusercontent.com/64240637/114295397-f5f83100-9adf-11eb-83f5-aebccd8f8072.png" width=700px, height=500px>


#### ```코드```
```py
def solution(a,b):
  answer = 0
  i = 0

  while True:
    if i == len(a):
      break
    answer += a[i] + b[i]
    i += 1
  
  return answer
```

#### ```질문```

- answer의 기본값이 ```answer=1234567890```으로 되어 있었지만 answer = 0으로 고친 후 문제를 풀었다. 기본값을 바꾸어도 괜찮은가?