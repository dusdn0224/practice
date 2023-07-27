# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print(f'반갑습니다. {self.name}입니다.')

# class Professor(Person):
#     def __init__(self, name, age, department):
#         # self.name = name
#         # self.age = age
#         # Person.__init__(self, name, age)
#         super().__init__(name, age)
#         self.department = department

# class Student(Person):
#     def __init__(self, name, age, gpa):
#         # self.name = name
#         # self.age = age
#         # Person.__init__(self, name, age)
#         super().__init__(name, age)
#         self.gpa = gpa

# p1 = Professor('박교수', 49, '컴퓨터공학과')
# s1 = Student('김학생', 20, 3.5)

# p1.talk()
# s1.talk()

# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def greeting(self):
#         return f'안녕, {self.name}'

# class Mom(Person):
#     gene = 'XX'

#     def swim(self):
#         return '엄마가 수영'

# class Dad(Person):
#     gene = 'XY'

#     def walk(self):
#         return '아빠가 걷기'

# class FirstChild(Mom, Dad):
#     def swim(self):
#         return '첫째가 수영'
    
#     def cry(self):
#         return '첫째가 응애'
    
# baby1 = FirstChild('아가')
# print(baby1.cry())
# print(baby1.swim())
# print(baby1.walk())
# print(baby1.gene)
# print(baby1.name)
# print(FirstChild.mro())

# try:
#     num = int(input('input: '))
#     print(100 / num)
# except ValueError:
#     print('input number')
# except ZeroDivisionError:
#     print('wht 0?')

# 클래스 Car정의, 부모클래스
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def info(self):
        print(f'Model: {self.model}, color: {self.color}')
# 클래스 CarDrive 정의, 자식 클래스
class CarDrive(Car):
    def speedchange(self, speed):
        self.speed = speed
        print(f'speedchange: {self.speed}')
car1 = CarDrive('Niro', 'Black')
# 1. info 메서드 호출
car1.info()
# 2. speedchange 메서드 호출
car1.speedchange(100)
# 자식클래스는 부모클래스의 클래스 변수와 메서드를 따로 선언하지 않아도 사용 가능

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

class CarDrive(Car):
    def __init__(self, model, color, speed):
        # 실습1. super() 내장함수 사용
        super().__init__(model, color)
        self.speed = speed
    
    def info(self):
        print(f'Model: {self.model}, color: {self.color}, speed: {self.speed}')

# 실습2. info 메서드 호출
car1 = CarDrive('Niro', 'Black', 100)
car1.info()
# super() 함수는 부모 클래스의 메서드를 호출하기 위해 사용

class Car:
    def __init__(self, model):
        self.model = model

class Hyundai(Car):
    color = 'white'
    
    def speed(self):
        return '80km/h'

class Kia(Car):
    color = 'black'

    def engine(self):
        return '1.6turbo'
    
class CarDrive(Hyundai, Kia):
    def speed(self):
        return '100km/h'
    def power(self):
        return '1.999cc'

car1 = CarDrive('HyunKi')
# speed 메서드 호출 -> 출력 -> 오버라이딩
print(car1.speed())
# engine 메서드 호출 -> 출력
print(car1.engine())
# power 메서드 호출 -> 출력
print(car1.power())
# color 클래스 변수 접근 -> 출력
print(car1.color)
print(car1.model)
print(CarDrive.mro())

# 오버라이딩: 부모 클래스의 메서드를 자식 클래스에서 재정의하는 것
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(f'Model: {self.model}, color: {self.color}')

class CarDrive(Car):
    # 실습1. info 메서드를 오버라이딩
    def info(self):
        print(f'\noverride\nModel: {self.model}, color: {self.color}')

# 실습2. info 메서드 호출
car1 = CarDrive('Niro', 'black')
car1.info()

# 디버깅 - NameError, TypeError, IndexError
def calculate_sum(a, b):
    return a + b
numbers = [1, 2, 3, 4, 5]
total_sum = 0
for i in range(len(numbers)):
    total_sum = calculate_sum(total_sum, numbers[i])
print(f'종합: {total_sum}')