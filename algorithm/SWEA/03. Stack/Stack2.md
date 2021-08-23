# 스택2

# 계산기

> 문자열로 된 계산식이 주어질 때, 스택을 이용하여 값을 계산할 수 있다
>
> * 중위표기법(infix notation) 
>
>   `A+B`
>
> * 후위표기법(postfix notation)
>
>   `AB+`

#### 문자열 수식 계산 방법

1. **중위 표기법의 수식을 후위 표기법으로 변경한다 (스택 이용)**

   1. 입력 받은 중위 표기식에서 토큰을 읽는다

   2. 토큰이 피연산자이면 토큰을 출력한다

   3.  토큰이 연산자일 때 스택의 `top`보다 우선순위가 높으면 스택에 `push`

      그렇지 않다면 스택 `top`의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에 `pop`한 후 토큰을 `push`

      만약 `top`에 연산자가 없으면 `push`

2. **후위 표기법의 수식을 스택을 이용하여 계산한다**

   1. 피연산자를 만나면 스택에 `push`한다

   2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 `pop`

      연산 결과를 다시 스택에 `push`

   3. 마지막으로 스택을 `pop`하여 출력한다

# 백트래킹(Backtracking)

> 해를 찾는 도중에 **막히면** 되돌아가서 다시 해를 찾아가는 기법
>
> 최적화(optimaization)문제와 결정(decision) 문제를 해결할 수 있다



#### 결정(decision) 문제 

> 문제의 조건을 만족하는 해가 존재하는 지의 여부를 'yes' or 'no' 로 답하는 문제

* 미로찾기
* n-Queen 문제
* Map coloring
* 부분집합의 합(Subset Sum) 문제 등

#### 깊이우선검색 vs. 백트래킹

* 깊이우선탐색 : 모든 경로를 추적
* 백트래킹 : 불필요한 경로 조기에 차단 (Prunning, 가지치기) -> 경우의 수가 많을 때

#### 백트래킹 기법

> 어떤 노드의 유망성을 점검한 후에 유망(Promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(Backtracking) 다음 자식 노드로 감

* 해답의 가능성이 있으면 유망

* 가지치기(Prunning) : 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않는다

1. 상태 공간 트리의 깊이 우선 검색을 실시한다
2. 각 노드가 유망한 지를 점검한다
3. 만일 그 노드가 유망하지 않다면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다

```python
def checknode(v):	# node
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)
```

# [참고] 부분집합, 순열

#### 부분집합

``` python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다
    else:
        k+=1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3)
```

#### 순열



# 분할정복

> 나플레옹이 사용한 전략에서 유래

#### 설계 전략

* 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다
* 정복(Conquer) : 나눈 작은 문제를 각각 해결한다
* 통합(Combine) : (필요하다면) 해결된 해답을 모은다