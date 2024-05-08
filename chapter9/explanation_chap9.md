## 정렬의 정의
: 원소들을 순서대로 배열하는 것

정렬은 알고리즘의 설계와 분석, 생각하는 방법 등을 훈련하기 좋은 구성요소를 많이 갖고 있다.

### 정렬 알고리즘과 평균 성능
![](https://velog.velcdn.com/images/chung0916/post/a6725b6e-fd1c-4aa5-8a37-310e4b818c2c/image.png)

---
</br>

## 기본 정렬 알고리즘
### 선택 정렬
#### 정의
선택 정렬이란 배열에서 최소값을 반복적으로 찾아 정렬하는 알고리즘이다.

#### 동작 방식
동작 방식은 3단계로 구성된다.

1️⃣ 주어진 배열에서 최소값을 찾는다.
2️⃣ 최소값을 맨 앞의 값과 바꾼다.
3️⃣ 바꿔준 맨 앞 값을 제외한 나머지 원소를 동일한 방법으로 바꿔준다.

#### 특징
✔️ 선택 정렬은 크게 2가지로 '최소 선택 정렬'과 '최대 선택 정렬'이 있다.

✔️ 최소는 오름차순으로 정렬하는 것이고, 최대는 내림차순으로 정렬하는 것이다.

#### 시간 복잡도와 공간 복잡도
⏰
시간 복잡도는 최선, 평균, 최악 모두 O(n^2)에 해당하는 비효율적인 알고리즘으로 정렬 여부와 상관없이 모든 경우의 수를 전부 확인한다.

👾
주어진 배열 안에서 교환(swap)을 통해, 정렬이 수행되므로 O(n) 이다



### 버블 정렬
#### 정의 
버블 정렬은 서로 인접해 있는 요소 간의 대소 비교를 통해 정렬한다.

#### 동작 방식
동작 방식은 인접한 두 요소간의 대소 비교를 진행한다.

#### 특징
버블 정렬은 정렬 알고리즘 중 가장 단순한 알고리즘으로, 단순한 만큼 비효율적이다.

#### 시간 복잡도와 공간 복잡도
⏰
시간 복잡도가 최고, 평균, 최악 모두 O(n^2)이다.

👾
공간 복잡도는 하나의 배열만 사용하므로 O(n)을 가진다.

### 삽입 정렬
#### 정의
삽입 정렬은 정렬을 진행할 원소의 index보다 낮은 곳에 있는 원소들을 탐색하여 알맞은 위치에 삽입해주는 정렬 알고리즘이다. 

#### 동작 방식
동작 방식은 두 번째 index부터 시작한다.
👉 그 이유는 첫 번째 index는 비교할 원소가 없기 때문이다.

#### 특징
알고리즘이 동작하는 동안 계속해서 정렬이 진행되므로 반드시 맨 왼쪽 index까지 탐색하지 않아도 된다는 장점이 있다.

#### 시간 복잡도와 공간 복잡도
⏰
모두 정렬되어 있는 최적의 경우, 모든 원소가 한 번씩만 비교되어 O(n)의 시간복잡도를 가진다.

👾
병렬 정렬은 추가적인 공간을 필요로 하여, 내부 정렬 (In-Place Sorting)이 아니다.
공간복잡도는 하나의 배열에서 정렬이 이루어지므로 O(n)이다.

---
</br>


## 고급 정렬 알고리즘
### 병합 정렬
#### 정의
병합 정렬은 분할정복과 재귀 알고리즘을 사용하는 정렬 알고리즘이다.

#### 동작 방식
1️⃣ 배열을 원소가 하나만 남을 때까지 계속 이분할을 한다.
2️⃣ 대소관계를 고려하여 다시 재배열하며 원래 크기의 배열로 병합한다. 

#### 특징
✔️ 퀵 정렬과 함께 두 개의 알고리즘이 사용된다는 측면에서 공통점을 가진다.

✔️ 퀵 정렬과 차이점으로는 동작 방식에 있다.

#### 시간 복잡도와 공간 복잡도
⏰
시간 복잡도는 최악, 평균, 최선의 모든 경우에 θ(n logn)이다.

👾
병합정렬의 공간복잡도는 O(n)이다.

### 퀵 정렬
#### 정의
퀵 정렬은 분할정복법과 재귀를 사용해 정렬하는 알고리즘이다.
선행 작업을 한 다음 재귀적으로 작은 문제를 해결하면서 바로 끝난다.

#### 동작 방식
1️⃣ 기준 원소를 하나 잡는다.
2️⃣ 기준 원소보다 작은 원소와 큰 원소의 그룹으로 나눈다.
3️⃣ 기준 원소의 좌우로 분할한 다음 각각을 정렬한다.

#### 특징
✔️ 왼쪽과 오른쪽의 정렬이 끝나는 순간 전체 리스트의 정렬이 끝난다.

✔️ 왼쪽과 오른쪽의 정렬에는 퀵정렬을 재귀적으로 사용한다.

#### 시간 복잡도와 공간 복잡도
⏰
✔️ 수행 시간은 평균 θ(n logn)이다.

✔️ 최악의 경우는 한쪽이 아예 없고 다른쪽에 다 몰리도록 분할되는 일이 반복되는 경우이고, 이때의 시간 복잡도는 θ(n^2)이다.

✔️ 한 쪽이 완전히 비지 않아도 분할이 대부분 극심하게 맞지 않으면 시간 복잡도는 역시 θ(n^2)가 된다.

👾
기존에 주어진 배열에서 원소 Swap만 이루어지므로 공간 복잡도는 O(n)


### 힙 정렬
#### 정의
힙 : 트리 기반의 자료구조로서, 두 개의 노드를 가진 완전 이진트리이다.

힙 정렬 : 완전 이진 트리를 기반으로 하는 정렬 알고리즘.


#### 동작 방식
(최대 힙의 경우)
1️⃣ 왼쪽 자식이 부모보다 작은지 확인한다.
2️⃣ 오른쪽 자식이 부모보다 작은지 확인한다.
3️⃣ 초기 index와 동일하지 않다면 부모 자식간의 상호 위치를 변경한 뒤 재귀를 반복한다.

#### 특징
✔️ 힙의 분류는 크게 '최대 힙'과 '최소 힙', 두 가지로 나뉜다.
👉 최대 힙은 내림차순 정렬에 사용하고, 최소 힙은 오름차순 정렬에 사용한다.

👉 최대 힙의 경우 부모 노드가 항상 자식 노드보다 크다.
👉 최소 힙의 경우 부모 노드가 항상 자식 노드보다 작다.

✔️ 힙은 부모 자식 간의 대소 관계만 나타나고, 좌우 관계는 나타내지 않는다.

✔️ 힙은 완전 이진 트리이기 때문에 적절히 중간 레벨의 노트를 추출하면 중앙값에 가까운 근사치로 빠르게 추출할 수 있다.
👉 힙은 배열 순서대로 표현하기 적절하다.

#### 시간 복잡도와 공간 복잡도
⏰
시간 복잡도는 최악, 평균의 경우에 θ(n logn)이다.
최선의 경우 (모든 원소가 동일한 경우) θ(n)시간에 끝난다.

👾
힙 정렬은 추가적인 공간을 요구하지 않아, 공간 복잡도는 O(n)이다.



### 셀 정렬
#### 정의
✔️ 삽입 정렬의 단점을 보완하고자 도입되었다.

✔️ 셸 정렬에 사용되는 핵심 개념은 interval (간격)이다. interval은 비교할 원소 간의 간격을 의미한다. 

✔️ 셸 정렬에서는 비교 횟수를 줄이기 위해 interval은 큰 값에서 낮은 값으로 낮춰간다. 

#### 동작 방식
1️⃣ 배열에서 interval 만큼 떨어진 원소들을 부분집합으로 구성한 뒤 삽입 정렬을 진행하는 방식으로 진행된다. 
2️⃣ 초기 interval 값은 len(array) // 2로 설정하며 계속 2로 나누어준다. 

#### 특징
✔️ 삽입 정렬은 주어진 정렬 상태가 역순으로 배열되어 있을수록 비교횟수가 늘어나고, 최선의 경우 O(n)이지만 최악의 경우 O(n^2)으로 성능 차이가 크다. 
👉 셸 정렬은 이러한 시간복잡도를 평균적으로 O(n^1.25) 또는 O(n^1.5) 수준으로 낮추고자 도입된 알고리즘이다.

#### 시간 복잡도와 공간 복잡도
⏰
시간복잡도는 평균 O(n^1.25)이고, 최악의 경우 O(n^1.5)이다.

👾
주어진 배열 안에서 교환을 통해 정렬이 이루어지기 때문에 공간 복잡도는 O(1)이다.

---
</br>

## 특수 정렬 알고리즘
<!-- 
### 계수 정렬
#### 정의

#### 동작 방식

#### 특징

#### 시간 복잡도와 공간 복잡도
⏰
👾
-->

### 기수 정렬
#### 정의
✔️ 기수 정렬은 non-comparison 알고리즘으로 원소간의 대소 비교를 하지 않고 정렬하는 알고리즘이다.

✔️ 대신 기수 정렬은 정렬하고자 하는 수의 낮은 자리 수를 차례대로 확인하여 정렬하는 방식이다. 


#### 동작 방식
1️⃣ 우선 가장 낮은 자릿수만으로 모든 수를 재배열(정렬)한다.
2️⃣ 둘째 자릿수를 대상으로 정렬한다.
3️⃣ 이어서 셋째 자릿 수에 대해 정렬한다.
4️⃣ 이를 반복하여, 작업을 완료한다.

#### 특징
안전성을 유지하면서 정렬한다.
👉값이 같은 원소끼리는 정렬 후에 원래의 순서가 바뀌지 않아야 한다. 

#### 시간 복잡도와 공간 복잡도
⏰
시간 복잡도는 θ(n)이다.

👾
공간 복잡도는 O(n)이다.

<!-- 
### 버킷 정렬
#### 정의

#### 동작 방식

#### 특징

#### 시간 복잡도와 공간 복잡도
⏰
👾
-->