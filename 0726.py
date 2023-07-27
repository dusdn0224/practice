# # 클래스 정의
# class Person:
#     # 속성(변수)
#     blood_color = 'red'

#     # 메서드
#     def __init__(self, name): # 생성자 메서드
#         self.name = name
    
#     def singing(self):
#         return f'{self.name}가 노래합니다.'

# # 인스턴스 생성
# singer1 = Person('iu')
# singer2 = Person('BTS')

# # 메서드 호출
# print(singer1.singing())
# print(singer2.singing())

# # 속성(변수) 사용
# print(singer1.blood_color)
# print(singer2.blood_color)

# singer1.gender = 'female'
# singer2.gender = 'male'
# print(singer1.gender)
# print(singer2.gender)

# # 객체 지향 프로그래밍: python, jave, c++, javascript
# # 메서드를 하나의 객체로 묶어 관리하는 프로그래밍 패러다임

# # 객체.메서드()
# print('abc'.upper())
# # 인스턴스? 인스턴스는 객체와 같은 말
# # 객체만 지칭할 때는 객체, 클래스와 연관지어 부를 때는 인스턴스
# # 인스턴스.메서드()

# class Person:
#     name = 'kai'
# # 실습1. 클래스 변수에 접근하여 kai를 출력해보세요.
# kai = Person() # 1. 인스턴스 생성(인스턴스 = 클래스())
# print(kai.name) # 2. 클래스 변수 호출(인스턴스.클래스 변수)
# # or
# print(Person.name)

# class Person:
#     def say(self):
#         print('Welcome!')
# # 실습2. say() 메서드를 호출해보세요.
# kai = Person() # 1. 인스턴스 생성
# kai.say() # 2. 인스턴스 메서드 호출

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def say(self):
#         print(f'Welcome! {self.name}')
# # 실습3. say() 메서드를 호출해보세요.
# person1 = Person('kai')
# person1.say()

# class Car:
#     model = 'Sonata'
#     color = 'white'
#     def speedchange(self, v):
#         print(f'speed: {v}')
#         self.speed = v

# # 실습1. Sonata 출력, white 출력, speed: 80 출력
# car1 = Car()
# print(car1.model)
# print(car1.color)
# car1.speedchange(80)

# # 실습2. ---> 생성자 메서드 구조로 바꾸기
# # model: Sonata, color: white, speed: 80
# class Car:
#     def __init__(self, model, color, speed):
#         print(f'model: {model}, color: {color}, speed: {speed}')
# car1 = Car('Sonata', 'white', 80)
# # or
# class Car:
#     def __init__(self, model, color, speed):
#         self.model = model
#         self.color = color
#         self.speed = speed
#     def info(self):
#         print(f'model: {self.model}, color: {self.color}, speed: {self.speed}')
# car1 = Car('Sonata', 'white', 80)
# car1.info()

# class Singer:
#     job = '가수'
#     birthdate = '1993년 05월 16일'
#     nation = '대한민국'
    
#     def __init__(self, name):
#         self.name = name
    
#     # def rap(self):
#     #     print(f'{self.name}이/가 랩을 한다 홍홍홍')
#     # def dance(self):
#     #     print(f'춤신춤왕 {self.name}')
#     # def sing(self):
#     #     print(f'소 몰고 가유')
    
#     # @classmethod
#     # def rap(cls):
#     #     print('랩을 한다 홍홍홍')
#     # @classmethod
#     # def dance(cls):
#     #     print(f'춤신춤왕')
#     # @classmethod
#     # def sing(cls):
#     #     print(f'소 몰고 가유')

#     @staticmethod
#     def rap():
#         print('랩을 한다 홍홍홍')
#     @staticmethod
#     def dance():
#         print(f'춤신춤왕')
#     @staticmethod
#     def sing():
#         print(f'소 몰고 가유')

# singer1 = Singer('IU')
# print(f'직업: {Singer.job}, 생년월일: {Singer.birthdate}, 국적: {Singer.nation}')
# # singer1.rap()
# # singer1.dance()
# # singer1.sing()
# Singer.rap()
# Singer.dance()
# Singer.sing()

# class Person:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Person.count += 1
# person1 = Person('에스파')
# person2 = Person('뉴진스')
# print(Person.count)

# class Circle:
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return 3.14 * self.r ** 2
#     def __str__(self):
#         return f'[원] radius: {self.r}'
# c1 = Circle(10)
# c2 = Circle(1)
# print(c1)
# print(c2)

def my_decorator(func):
    def wrapper():
        print('함수 실행 전')
        result = func()
        print('함수 실행 후')
        return result
    return wrapper

@my_decorator
def my_function():
    print('원본 함수 실행')

my_function()