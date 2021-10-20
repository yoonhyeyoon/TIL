# 03. many_to_many

> 2021.10.20

## ManyToManyField

* 다대다 (M:N) 관계 설정 시 사용하는 모델 필드
* 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
* `add()` `remove()` , ...

> [RelatedManager] 일대다 또는 다대다 관련 컨텍스트에서 사용되는 manager

##### ManyToManyField's Arguments

1. `related_name`

* 역참조시 사용할 manager의 이름을 설정
* ForeignKey의 related_name과 동일

2. `through`

* 중개 테이블을 직접 작성하는 경우 지정 가능
* 주로 다대다 관계 연결에서 사용된다

3. `symmetrical`

* ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
* True일 경우 대칭

##### Related Manager

`add()`

`remove()`

#### 중개 테이블의 필드 생성 규칙

1. source model != target model

* id
* <containing_model>_id
* <other_model>_id

2. source model == target model

* id
* `from_<model>_id`
* `to_<model>_id`