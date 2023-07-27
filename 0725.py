
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set) # {1, 2, 3, 4}
# my_set.add(4)
# print(my_set) # {1, 2, 3, 4} (중복은 추가 안 됨)

# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set) # set()

# my_set = {1, 2, 3}
# my_set.remove(2)
# print(my_set) # {1, 3}
# # my_set.remove(10) # KeyError

# my_set = {1, 2, 3}
# my_set.discard(2) # {1, 3}
# print(my_set)
# my_set.discard(10) # 에러 없음, None type

# my_set = {1, 2, 3}
# element = my_set.pop() # hash 문서 참고
# print(element) # 1
# print(my_set) # {2, 3}

# my_set = {1, 2, 3}
# my_set.update([4, 5, 1])
# print(my_set) # {1, 2, 3, 4, 5}

# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 3, 5, 7, 9}

# print(set1.difference(set2)) # {0, 2, 4} # set1 - set2
# print(set1.intersection(set2)) # {1, 3} # set1 & set2
# print(set1.issubset(set2)) # False # set1 <= set2
# print(set1.issuperset(set2)) # False # set1 >= set2
# print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9} # set1 | set2



# person = {'name': 'Alice', 'age': 25}
# person.clear()
# print(person) #{}

# person = {'name': 'Alice', 'age': 25}
# print(person.get('name')) # Alice
# print(person.get('country')) # None
# print(person.get('country', 'Unknown')) # Unknown

# person = {'name': 'Alice', 'age': 25}
# print(person.keys()) # dict_keys(['name', 'age'])
# for k in person.keys():
#     print(k)
# """
# name
# age
# """

# person = {'name': 'Alice', 'age': 25}
# print(person.values()) # dict_values(['Alice', 25])
# for v in person.values():
#     print(v)
# """
# Alice
# 25
# """

# person = {'name': 'Alice', 'age': 25}
# print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
# for k, v in person.items():
#     print(k, v)
# """
# name Alice
# age 25
# """

# person = {'name': 'Alice', 'age': 25}
# print(person.pop('age')) # 25
# print(person) # {'name': 'Alice'}
# # print(person.pop('country')) # KeyError
# print(person.pop('country', '그런 키는 없어요')) # 그런 키는 없어요

# person = {'name': 'Alice', 'age': 25}
# print(person.setdefault('name', 'Korea')) # Alice
# print(person.setdefault('country', 'Korea')) # Korea
# print(person) # {'name': 'Alice', 'age': 25, 'country': 'Korea'}

# person = {'name': 'Alice', 'age': 25}
# other_person = {'name': 'Jane', 'gender': 'Female'}
# person.update(other_person)
# print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}
# person.update(age = 50)
# print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}
# person.update(country = 'Korea')
# print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'Korea'}



# # 혈액형 인원수 세기
# # 결과 => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# # []
# new_dict = {}
# # blood_types를 순회하면서
# for blood_type in blood_types:
#     # 기존에 키가 이미 존재한다면,
#     if blood_type in new_dict:
#         # 기존 키의 값을 +1 증가
#         new_dict[blood_type] += 1
#     # 키가 존재하지 않는다면 (처음 설정되는 키)
#     else:
#         new_dict[blood_type] = 1
# print(new_dict)

# # .get()
# new_dict = {}
# # blood_types를 순회하면서
# for blood_type in blood_types:
#     new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
# print(new_dict)

# #.setdefault()
# new_dict = {}
# # blood_types를 순회하면서
# for blood_type in blood_types:
#     # new_dict.setdefault(blood_type, 0)
#     # new_dict[blood_type] += 1
#     new_dict[blood_type] = new_dict.setdefault(blood_type, 0) + 1
# print(new_dict)
