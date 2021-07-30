# OOP II

1. 상속(Inheritance)
2. 메서드 오버라이딩(Method Overriding)
3. 다중 상속(Multiple Inheritance)

# 1. 상속

* 상속(Inheritance)이란?

  * 클래스에서 가장 큰 특징은 `상속`이 가능하다는 것
  * 코드 재사용성이 높아진다

  ```python
  class ChildClass(ParentClass):
      <code block>
  ```

* `issubclass(class, classinfo)`

  * class가 classinfo의 subclass면 True

* `isinstance(object, classinfo)`

  * object가 classinfo의 인스턴스거나 subclass인 경우 True

* `super()`

  * 부모 클래스의 내용을 사용하고자 할 때

  ```python
  class ChildClass(ParentClass):
      def method(self, arg):
          super().method(arg) # 부모 메서드 가져오기
  ```

  

# 2. 메서드 오버라이딩

> Method Overriding(메서드 오버라이딩): 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것
>
> - 상속 받은 클래스에서 **같은 이름의 메서드**로 덮어씀

* 상속관계에서의 이름공간
  * 인스턴스 -> 자식 클래스 -> 부모 클래스

# 3. 다중 상속

* 두개 이상의 클래스를 상속받는 경우
* 상속 받은 모든 클래스의 요소 활용 가능
* 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정