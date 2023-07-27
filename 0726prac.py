# ws_7_1.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
      self.width = width
      self.height = height

shape1 = Shape(5, 3)
print(shape1.width, shape1.height)

# ws_7_2.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height

shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)

# ws_7_3.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)

# ws_7_4.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def print_info(self):
        print(f'Width: {self.width}\nHeight: {self.height}\nArea: {self.width * self.height}\nPerimeter: {2 * (self.width + self.height)}')

shape1 = Shape(5, 3)
shape1.print_info()

# ws_7_5.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'

shape1 = Shape(5, 3)
print(shape1)

# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, number, string):
        for i in range(number):
            print(string)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")

# hw_7_4.py

# 아래 클래스를 수정하시오.
class Person:
    number_of_people = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.number_of_people += 1
    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')

person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
