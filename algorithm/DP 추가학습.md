# DP 추가학습 (피보나치 예시)

### 1. 구하고 싶은 값이 N, list 에 N개 원소를 미리 할당

**dp = [0] * (N+1)**

- 초기값 설정 (DP 는 초기값이 있어야 함)

  DP[0] = 0

  DP[1] = 1

- 내가 구하고 싶은 N 까지 loop

   ```python
  dp = [0] * (N + 1)
  dp[0] = 0
  dp[1] = 1
  for i in range(2, N+1):
      dp[i] = dp[i-1] + dp[i-2]
  
  print(dp[N])
  ```

  

### 2. 그 순간순간 append() 하기

- 구현

  ````python
  dp = [0, 1]
  
  for i in range(2, N+1):
      dp.append(dp[i-1][i-2])
  ````

  

### 3.  필요 부분만 가지고 가기

- 저장할 필요도 없이, 갱신한다.

  ```python
  a, b = 0, 1 # a = dp[0], b = dp[1] 과 같은 의미
  for _ in range(2, N+1):
      a, b = b, a+b
  print(b)
  ```

  