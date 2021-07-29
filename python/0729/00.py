# oop

# 개의 속성과 행위를 정의하는 Doggy 클래스 만들기

# 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
# 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
# 개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
# 개가 죽으면 num_of_dogs의 값이 1 감소한다.
# 개는 각자의 이름과 나이가 있다.
# bark() 메서드를 호출하면 개는 짖을 수 있다.
# get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다.

class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, dog_type):
        self.name = name
        self.dog_type = dog_type
        self.age = 1
        Doggy.birth()
    
    def bark(self):
        print("왈왈!")
    
    @classmethod
    def birth(cls):
        cls.num_of_dogs += 1
        cls.birth_of_dogs += 1 
    
    @classmethod
    def dead(cls):
        cls.num_of_dogs -= 1
    
    def __del__(self):
        Doggy.dead()
        
    
    @classmethod
    def get_status(cls):
        print(f"Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}")



d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

d1.bark() #=> 왈왈!
d2.bark() #=> 왈왈!
d3.bark() #=> 왈왈!

Doggy.get_status() #=> Birth: 3, Current: 3