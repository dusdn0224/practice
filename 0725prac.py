
# # 세트: 가변형 비시퀀스 -> 중복 허용 X -> 집합과 같은 특징
# list1 = [1, 2, 3]
# list2 = [4, 5, 6, 7, 8, 9]
# set1 = set(list1)
# set2 = set(list2)

# # 1. set1에 4 추가
# set1.add(4)
# print(set1)
# # 2. set1에 [5, 6, 7] 추가
# set1.update([5, 6, 7])
# print(set1)
# # 3. set1에서 7 제거(2가지 방법)
# set1.remove(7)
# set1.discard(7)
# print(set1)
# # 4. set1 차집합 set2 출력(2가지 방법)
# print(set1 - set2)
# print(set1.difference(set2))
# # 5. set1 교집합 set2 출력(2가지 방법)
# print(set1 & set2)
# print(set1.intersection(set2))
# # 6. set1 합집합 set2 출력(2가지 방법)
# print(set1 | set2)
# print(set1.union(set2))
# '''

# '''
# # set.pop() -> 주소값이 작은 것부터 제거
# set1 = {1, 2, 3, 4, 5, 6}
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())



# dict1 = {
#     'plus': ['더하기', '장점'],
#     'minus': ['빼기', '적자'],
#     'multiply': ['곱하기', '다양하게'],
#     'division': ['나누기', '분열']
# }
# # 실습1. 영어 단어를 입력하면 단어의 뜻을 보여주는 프로그램(3가지 방법)
# # 1
# def dictionary1(word):
#     return dict1[word]
# # 2
# def dictionary2(word):
#     return dict1.get(word)
# # 3
# def dictionary3(word):
#     return dict1.setdefault(word)
# # 실습2. 영한사전에서 단어들의 목록을 출력
# for k in dict1.keys():
#     print(k)
# # 실습3. 다음 단어와 뜻을 추가하고 사전에 있는 모든 단어와 뜻을 출력(4가지 방법)
# #        'square': ['제곱', '사각형']
# # 1
# dict1['square'] = ['제곱', '사각형']
# for k, v in dict1.items():
#     print(k, v)
# # 2
# dict1['square'] = dict1.get('square', ['제곱', '사각형'])
# for k, v in dict1.items():
#     print(k, v)
# # 3
# dict1.setdefault('square', ['제곱', '사각형'])
# for k, v in dict1.items():
#     print(k, v)
# # 4
# new_dict = {'square': ['제곱', '사각형']}
# dict1.update(new_dict)
# for k, v in dict1.items():
#     print(k, v)
# # 실습4
# word = input()
# dict1.pop(word)
# print(dict1)


# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# # 출력 결과가 {'A': 3, 'B': 3, 'O': 3, 'AB': 3}이 나오게
# # counter 메서드를 사용하여 실습 진행
# from collections import Counter
# print(Counter(blood_types))

# # 할당, 얕은 복사, 깊은 복사
# # 불변 데이터 원본 변경 X, 가변 데이터

# # 1. 할당: 원본 데이터 변경 O
# list1 = [1, 2, 3, 4]
# list2 = list1
# list2[0] = 5
# print(id(list1), id(list2))
# print(list1, list2)

# # 2. 얕은 복사(슬라이싱, copy()): 객체 안에 객체가 있는 경우 원본 데이터가 변경 O
# list1 = [1, 2, [3, 4]]
# list2 = list1[:]
# list2 = list1.copy()
# list2[0] = 5
# list2[2][0] = 5
# print(id(list1), id(list2))
# print(id(list1[2]), id(list2[2]))
# print(list1, list2)

# # 3. 깊은 복사: 원본 데이터 변경 X
# import copy
# list1 = [1, 2, [3, 4]]
# list2 = copy.deepcopy(list1)
# list2[0] = 5
# list2[2][0] = 5
# print(id(list1), id(list2))
# print(id(list1[2]), id(list2[2]))
# print(list1, list2)

# # ws_6_1.py

# # 아래 함수를 수정하시오.
# def union_sets(set1, set2):
#     set1.update(set2)
#     return set1

# result = union_sets({1, 2, 3}, {3, 4, 5})
# print(result)

# # ws_6_2.py

# # 아래 함수를 수정하시오.
# def get_value_from_dict(dict1, key):
#     return dict1.get(key)

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_value_from_dict(my_dict, 'name')
# print(result) # Alice

# # ws_6_3.py

# # 아래 함수를 수정하시오.
# def intersection_sets(set1, set2):
#     return set1.intersection(set2)

# result = intersection_sets({1, 2, 3}, {3, 4, 5})
# print(result) # {3}

# # ws_6_4.py

# # 아래 함수를 수정하시오.
# def get_keys_from_dict(dict1):
#     return list(dict1.keys())

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_keys_from_dict(my_dict)
# print(result)

# # ws_6_5.py

# # 아래 함수를 수정하시오.
# def difference_sets(set1, set2):
#     return set1.difference(set2)

# result = difference_sets({1, 2, 3}, {3, 4, 5})
# print(result)

# # hw_6_2.py

# # 아래 함수를 수정하시오.
# def remove_duplicates_to_set(list1):
#     return set(list1)
		
# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)

# # hw_6_4.py

# # 아래 함수를 수정하시오.
# def add_item_to_dict(dictionary, key, value):
#     new_dict = dictionary.copy()
#     new_dict.setdefault(key, value)
#     return new_dict

# my_dict = {'name': 'Alice', 'age': 25}
# result = add_item_to_dict(my_dict, 'country', 'USA')
# print(result)
