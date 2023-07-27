# ws_8_1.py

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1

class Cat(Animal):
    def __init__(self):
        Animal.num_of_animal += 1

class Pet(Dog, Cat):
    def access_num_of_animal():
        return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'

dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())

# ws_8_2.py

# 아래 클래스를 수정하시오.
class Dog(Animal):
    def bark(self):
        print('멍멍!')

dog1 = Dog()
dog1.bark()

# ws_8_3.py

# 아래 클래스를 수정하시오.
class Cat(Animal):
    def meow(self):
        print('야옹!')

cat1 = Cat()
cat1.meow()

# ws_8_4.py

class Pet(Dog, Cat):
    def __init__(self, sound):
        self.sound = sound
    
    def make_sound(self):
        print(self.sound)
    
    def play(self):
        print('애완동물과 놀기')

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()

# ws_8_5.py

class Dog:
    sound = '멍멍'
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

class Cat:
    sound = '야옹'
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

class Pet(Dog, Cat):
    def __str__(self):
        return f'{Dog()}\n{Cat()}'

pet1 = Pet()
print(pet1)

# hw_8_2.py

# 아래 함수를 수정하시오.
def check_number():
    try:
        n = float(input('숫자를 입력하세요: '))
        if n > 0:
            print('양수입니다.')
        elif n < 0:
            print('음수입니다.')
        else:
            print('0입니다.')
    except ValueError:
        print('잘못된 입력입니다.')

check_number()

# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        self.name = input('이름을 입력하세요: ')
        self.user_data.setdefault('이름', self.name)
        try:
            self.age = int(input('나이를 입력하세요: '))
            self.user_data.setdefault('나이', self.age)
        except:
            print('나이는 숫자로 입력해야 합니다.')

    def display_user_info(self):
        try:
            print(f'사용자 정보:\n이름: {self.user_data["이름"]}\n나이: {self.user_data["나이"]}')
        except:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()
