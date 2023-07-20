# 함수 정의, 함수 선언

'''
def 함수명(매개변수):
    code....
    code....    # 함수 바디
    return 반환값
'''

# 함수 호출
'''
함수명(함수인자)
'''

# 매개변수는 있을 수도 있고 없을 수도 있다
# 반환값은 있을 수도 있고 없을 수도 있다
# -> 총 4가지 유형의 함수 존재

# def get_sum(num1, num2):
#     return num1 + num2
# num1 = 5
# num2 = 3
# result = get_sum(num1, num2)
# print(result)

# # 1. 매개변수가 없는 함수로 변형
# def get_sum():
#     num1, num2 = 5, 3
#     return num1 + num2
# result = get_sum()
# print(result)

# # 2. return 반환 값이 없는 함수로 변형
# def get_sum(num1, num2):
#     print(num1 + num2)
# num1 = 5
# num2 = 3
# get_sum(num1, num2)

# # 위치(Positional) 인자
# def greet(name, age):
#     print(f'안녕하세요, {name}님! {age}살이시군요.')
# greet('Alice', 25)

# # 기본(Default) 인자
# # 기본 인자는 뒤에서부터 할당
# def greet(age, name = 'Alice'):
#     print(f'안녕하세요, {name}님! {age}살이시군요.')
# greet(40)
# greet(40, 'Charlie')

# # 키워드 인자 -> 키워드인자와 위치인자는 같이 사용 불가
# def greet(name, age):
#     print(f'안녕하세요, {name}님! {age}살이시군요.')
# greet(name = 'Kai', age = 33)
# greet(age = 33, name = 'Kai')
# greet('Kai', age = 33)

# # 가변 인자 목록 -> 여러개의 인자를 tuple로 처리
# # 매개변수 앞에 *(애스터리스크)
# def calculate_sum(*args):
#     print(args)
#     total = sum(args)
#     print(f'합계: {total}')
# calculate_sum(1, 2, 3, 4, 5)

# # 가변 키워드 인자
# def print_info(**kwargs):
#     print(kwargs)
# print_info(name = 'dldusdn', age = 29, h = 182)

# z = 3 # global scope
# def outer():
#     x = 1 # local scope
#     def inner():
#         y = 2 # local scope
#         result = x + y # 여기선 x가 enclosed scope
#         print(result)
#     inner()
# outer()
# #built-in scope -> 내장함수 len(), print(), input() 등

# list_1 = [1, 2, 3, 4]
# print(sum(list_1)) # sum은 built-in scope
# sum = 5 # global scope
# print(sum)
# print(sum(list_1))

# a, b, c = 1, 2, 3
# def enclosed():
#     # global a, b, c
#     a, b, c = 4, 5, 6
#     def local(c):
#         print(a, b, c)
#     local(500)
#     print(a, b, c)
# enclosed()
# print(a, b, c)

# # 재귀함수 -> 정의: 자기자신을 호출하는 함수
# # 종료 조건을 반드시 포함할 것
# def fact(n):
#     if n == 0:    # 종료 조건
#         return 1
#     return n * fact(n-1)    # 반복되는 호출이 종료조건을 향하도록
# result = fact(6)
# print(result)

# # map(function, iterable)
# a = list(map(int, '12345678'))
# print(a)

# # zip(*iterables) -> *iterables를 튜플을 원소로 하는 zip객체 반환
# names = ['a', 'b', 'c']
# ages = [30, 40, 50]
# cities = ['x', 'y', 'z']
# for name, age, city in zip(names, ages, cities):
#     print(name, age, city)

# lambda 매개변수: 표현식
# 1. 1회성이기때문에 함수 명이 필요없다
# 2. 표현식의 결과가 반환
'''
map() 함수를 사용하여
numbers 리스트의 각 요소가
제곱된 값들로 이루어진
새로운 리스트 생성
'''
# # numbers = [1, 2, 3, 4, 5]
# # square = list(map(lambda x: x * x, numbers))
# # print(square)

# # 패킹: 여러 값을 하나의 시퀀스로 묶는 과정
# # 예시 1)
# packing_values = 1, 2, 3, 4, 5
# print(packing_values)

# numbers = [1, 2, 3, 4, 5]
# a, *b, c = numbers # *(애스터리스크): 패킹연산자로 활용
# print(a)
# print(b)
# print(c)

# print('hi', 'hello', 'goodbye', sep = '-')

# # *(애스터리스크)를 언패킹 연산자로 활용
# name = ['aaa', 'bbb', 'ccc']
# print(*name)

# # **: 딕셔너리 언패킹 연산자
# def my_function(x, y, z):
#     print(x, y, z)
# dict_values = {'x': 1, 'y': 2, 'z': 3}
# my_function(**dict_values)

# import math
# print(math.pi)
# print(math.sqrt(4))

# from math import pi, sqrt
# print(pi)
# print(sqrt(4))

# import random
# print(random.randint(1, 10))

# from random import *
# print(randint(1, 10))

# import my_math
# print(my_math.add(1, 2))

# from my_package.math import my_math
# from my_package.statistics import tools
# print(my_math.add(1, 2))
# print(tools.mod(1, 2))

import requests
url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()
# print(response)

# 실습) United States를 출력해보세요.
print(response['address']['country'])