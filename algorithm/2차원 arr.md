# 2차원 배열

### 2차원 리스트 입력받기

```python
N, M = map(int, input().split())

# 1번
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 2번
arr = [list(map(int, input().split())) for _ in range(N)]    

for i in arr:
    print(i)
```



### 배열 순회 : n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

- **행 우선 순회**

```python
# i 행의 좌표
# j 열의 좌표

for i in range(len(Array)):
    for j in range(len(Array[i])):
        Array[i][j] # 필요한 연산 수행
```

- **열 우선 순회**

```python
# i 행의 좌표
# j 열의 좌표

for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j] # 필요한 연산 수행
```

- **행 우선 순회를 역으로**

```python
# i 행의 좌표
# j 열의 좌표

for i in range(len(Array)):
    for j in range(len(Array[i])-1, -1, -1):
        Array[i][j] # 필요한 연산 수행
```

- **지그재그 순회**

```python
# i 행의 좌표
# j 열의 좌표

for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j + (m-1-2*j)*(i*2)]
        # 필요한 연산 수행
```



### 2차원 배열의 활용

- **델타이동**

```python
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]

r= 1
c= 1

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

drc = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]
    
    # if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
    # print(arr[nr][nc])
    
    if 0 <= nr < N and 0 <= nc < N:
        print(arr[nr][nc])
```

- **전치행렬**

```python
# i: 행의 좌표, len(arr)
# j: 열의 좌표, len(arr[0])
arr = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```



### 부분집합

- **부분집합 만들기**

```python
bit = [0,0,0,0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(*bit)
```



### 비트 연산자

- **비트 연산자**

1. `&` 비트 단위로 AND 연산을 한다.

   ex) 0110 & 1011 = 0010 

   ex) print(6 & 11) # 2

2. `|` 비트 단위로 OR 연산을 한다

   ex) 0110 | 1011 = 1111

   ex) print(6 | 11) # 15

3. `<<` 피연산자의 비트 열을 왼쪽으로 이동시킨다.

4. `>>` 피연산자의 비트 열을 오른쪽으로 이동시킨다.



- **<<  연산자**

1 << n: 2**n 즉, 원소가 n 개일 꼉우의 모든 부분집합의 수를 의미

<< 한번 할때마다 값이 2배씩 증가함

ex) 2 << 3 = 2 * 2* 2* 2 = 16



- **& 연산자**

i & (1 << j) : i 의 j 번째 비트가 1인지 아닌지를 리턴한다.



```python
arr = [3,6,7,1,5,4]

n = len(arr)

for i in range(1<<n):
    ans = ""
    for j in range(n):
        if i & (1<<j):
           ans += str(arr[j]) + ""
    print(ans)
```

