# # ws_5_1.py

# def reverse_string(list):
#     result = ''.join(reversed(list)) # 뒤집어서 join 함수 사용 str 만들기
#     return result # 값 반환

# result = reverse_string("Hello, World!")
# print(result)

# # ws_5_2.py

# # 아래 함수를 수정하시오.
# def remove_duplicates(list):
#     new_lst = []
#     for i in range(1, list[len(list) - 1] + 1): # 1부터 list의 마지막 원소까지 반복
#         new_lst.append(list[list.index(i)]) # 각 원소를 중복되지 않게 추가
#     return new_lst

# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# # ws_5_3.py

# # 아래 함수를 수정하시오.
# def sort_tuple(tup):
#     new_tuple = ()
#     tup = list(tup)
#     tup.sort()
#     new_tuple += tuple(tup)
#     return new_tuple

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)

# # ws_5_4.py

# # 아래 함수를 수정하시오.
# def capitalize_words(string):
#     return string.title()

# result = capitalize_words("hello, world! wow pakapke ajossiya")
# print(result)

# # ws_5_5.py

# # 아래 함수를 수정하시오.
# def even_elements(my_list):
#     for i in my_list:
#         if i % 2 == 1:
#             my_list.pop(my_list.index(i))
#     new_list = []
#     new_list.extend(my_list)
#     return new_list

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)

# # main.py

# # 아래 함수를 수정하시오.
# def count_character(string, char):
#     return string.count(char)

# result = count_character("Hello, World!", "o")
# print(result) # 2

# # main.py

# # 아래 함수를 수정하시오.
# def find_min_max(mylist):
#     mylist.sort()
#     return mylist[0], mylist[len(mylist) - 1]

# result = find_min_max([3, 1, 7, 2, 5])
# print(result) # (1, 7)
