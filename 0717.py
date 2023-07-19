# a1 = 1
# a2 = 2.3
# a3 = 2 + 3j
# a4 = 'hello world'
# a5 = [1, 2, 3, 4]
# a6 = (1, 2, 3, 4)
# a7 = range(1, 5)
# a8 = {1, 2, 3, 4}
# a9 = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# a10 = None
# a11 = True
# a12 = lambda x, y : x + y

# for i in range(1, 13):
#     var = f'a{i}'
#     var = eval(var)
#     print(type(var))

# print('7/3 : ', 7/3, '\n7//3 : ', 7//3, '\n7%3 : ', 7%3)

# print(-2 ** 4)
# print(-(2 ** 4))
# print((-2) ** 4)

# for i in range(1,13):
#     print(id(f'a{i}'))

# degrees = 36.5
# print(id(degrees))

# degrees = 37.5
# print(id(degrees))

# number = 10
# double = 2 * number
# print(double)

# numer = 5
# print(double)

# is_number = True
# SECOND = 10
# PI = 3.14
# name = 'lee'
# my_name = 'yeon woo'

# my_list = [
#     1, 2, 3,
#     4, 5, 6
# ]

# char = input('문자 한 개를 입력하세요: ')
# cdlist = list(map(int, input().split('.')))
# print(cdlist[0], cdlist[1])

# name = input()
# age = int(input())
# height = float(input())

# # 1. 포맷 코드
# print('저의 이름은 %s, 나이는 %d, 키는 %.2f' %(name, age, height))

# # 2. f-string
# print(f'저의 이름은 {name}, 나이는 {age}, 키는 {height: .2f}')

# # 3. .format()
# print('저의 이름은 {}, 나이는 {}, 키는 {}'.format(name, age, height))

# string = '문자열'
# integer = 10
# floating_point = 3.14
# a_list = [1, 2, 3, 4, 5]
# dictionary = {'name': '홍길동', 'age': 20}
# a_set = {1, 2, 3, 4, 5}
# a_range = range(11)
# a_tuple = (1, 2, 3)
# boolean = True

# print(type(string))
# print(type(integer))
# print(type(floating_point))
# print(type(a_list))
# print(type(dictionary))
# print(type(a_set))
# print(type(a_range))
# print(type(a_tuple))
# print(type(boolean))

# print()

# print(type(string) == str)
# print(type(integer) == int)
# print(type(floating_point) == float)
# print(type(a_list) == list)
# print(type(dictionary) == dict)
# print(type(a_set) == set)
# print(type(a_range) == range)
# print(type(a_tuple) == tuple)
# print(type(boolean) == bool)

# a1 = '반짝 반짝'
# a2 = '에서도'
# a3 = '작은별'
# a4 = '아름답게 비치네'
# a5 = '동쪽 하늘'
# a6 = '서쪽 하늘'

# print(a1, a3, a4)
# print(a5 + a2, a6 + a2)
# print(a1, a3, a4)

# # 원주율
# PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# # 반지름
# r = 15

# a1 = '원주율 : '
# a2 = '반지름 : '
# a3 = '원의 둘레 : '
# a4 = '원의 넓이 : '

# print(a1, PI)
# print(a2, r)
# print(a3, r * 2 * PI)
# print(a4, r ** 2 * PI)

# print(3 * 2)
# print(3 ** 2)
# print((3 ** 2) // (3 * 2), (3 ** 2) % (3 * 2))
# print(3 ** 2 + -3 ** 2)

# a = 3

# print(a * 2)
# print(a ** 2)
# print((a ** 2) // (a * 2), (a ** 2) % (a * 2))
# print(a ** 2 + -a ** 2)

# apple =  '사과는 영어로 apple'
# banana = '바나나는 영어로 banana'
# kiwi = '키위는 영어로 kiwi'
# print(apple)
# print(banana)
# print(kiwi)

# print(pi)

# T = int(input())
# for test_case in range(1, T + 1):
#     a = list(map(int, input().split()))
#     for i in range(9):
#         if a[ i ] > a[ i + 1 ]:
#             a[ i + 1 ] = a[ i ]
#     print(f'#{test_case}', a[9])

# import calendar
# calendar.prmonth(2023, 7)

# N = int(input())
# a = list(map(int, input().split()))
# a.sort(reverse=True)
# print(a[(N // 2) + 1])
# print(a)

# a, b = map(int, input().split())
# if a - b == 1 or a - b == -2:
#     print('A')
# else:
#     print('B')

# import calendar
# dir(calendar)
# calendar.prmonth(1996, 2)

# T = int(input())
# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
#     nlist = list(map(int, input().split()))
#     mlist = list(map(int, input().split()))
#     rlist = []
#     h = 0
#     p = 0
#     if n < m:
#         while p <= m - n:
#             for i in range(n):
#                 k = nlist[i] * mlist[i + p]
#                 h += k
#             rlist.append(h)
#             h = 0
#             p += 1
#         rlist.sort()
#         print(f'#{test_case}', rlist[m - n])
#     elif n > m:
#         while p <= n -m:
#             for i in range(m):
#                 k = nlist[i + p] * mlist[i]
#                 h += k
#             rlist.append(h)
#             h = 0
#             p += 1
#         rlist.sort()
#         print(f'#{test_case}', rlist[n - m])
#     elif n == m:
#         for i in range(n):
#             k = nlist[i] * mlist[i]
#             h += k
#         print(f'#{test_case}', h)