# List Comprehension
# [expression for 변수 in iterable]
# list(expression for 변수 in iterable)

# # 0 ~ 9 리스트 만들기
# # 1. 일반적인 방법
# new_list = []
# for i in range(10):
#     new_list.append(i)
# print(new_list)

# # 2. List Comprehension
# new_list_2 = [i for i in range(10)]
# print(new_list_2)

# # 홀수만
# new_list = []
# for i in range(10):
#     if i % 2 == 1:
#         new_list.append(i)
# print(new_list)

# new_list_2 = [i for i in range(10) if i % 2 == 1]
# print(new_list_2)

# # if - else
# new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
# print(new_list_3)
# # elif는 안 됨
# # if 중첩은 됨

# 리스트를 생성하는 3가지 방법 비교
# 정수 1, 2, 3을 가지는 새로운 리스트 만들기
# 어떤게 제일 빨라요?

# numbers = ['1', '2', '3']

# # 1. for loop
# new_numbers = []
# for number in numbers:
#     new_numbers.append(int(number))
# print(new_numbers)

# # 2. map
# new_numbers_2 = list(map(int, numbers))
# print(new_numbers_2)

# # 3. list comprehension
# new_numbers_3 = [int(number) for number in numbers]
# print(new_numbers_3)

# # enumerate
# result = ['a', 'b', 'c']
# print(enumerate(result))
# print(list(enumerate(result)))

# for index, elem in enumerate(result):
#     print(index, elem)