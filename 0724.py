# print(help(list))

# print('hello world'.capitalize())
# print('hello world'.title())

# print('banana'.find('a'))
# print('banana'.find('z'))
# print('banana'.index('a'))
# # print('banana'.index('z'))
# print('BANANA'.isupper())
# print('banana'.isupper())
# print('Banana'.isupper())
# print('banana'.islower())
# print('BANANA'.islower())
# print('Banana'.islower())
# print('banana'.isalpha())
# print('123'.isalpha())

# t = 'Hello, world!'
# new_t = t.replace('world', 'Python')
# t = '   Hello, world!    '
# print(t)
# new_t = t.strip()
# print(new_t)
# words = t.split(',')
# print(words)
# text = '-'.join(words)
# print(text)

# ml = [1, 2, 3, 4, 5]
# # ml.append([4, 5, 6])
# # ml.extend([4, 5, 6])
# # ml.insert(1, 5)
# # ml.remove(2)
# i1 = ml.pop()
# i2 = ml.pop(0)
# print(ml)
# print(i1, i2)

# ml2 = [1, 2, 2, 3, 3, 3]
# c = ml2.count(3)
# print(c)

# ml3 = [1, 4, 6, 7, 2, 3, 9]
# ml3.sort()
# ml3.reverse()
# print(ml3)

# # sort 매서드
# numbers = [2, 3, 1]
# print(numbers.sort()) # None

# #sorted 함수
# numbers = [2, 3, 1]
# print(sorted(numbers)) # [1, 2, 3]
# print(numbers) # [2, 3, 1]

# numbers = [1, 2, 3]
#  # 1. 할당
# list1 = numbers

# # 2. 슬라이싱
# list2 = numbers[:]

# numbers[0] = 100

# print(list1)
# print(list2)

# a = 'Practice makes perfect'
# # 1. 문자열 a에서 'e'의 개수 세기
# print(a.count('e'))
# # 2. 문자열 a에서 'i'의 위치 찾기(2가지 방법)
# print(a.find('i'))
# print(a.index('i'))
# # 3. 문자열 a의 문자 사이에 .(점) 삽입
# print('.'.join(a))
# # 4. 문자열 a를 공백 기준으로 분리하여 출력
# print(a.split())
# # 5. 문자열 a에서 'makes'를 'made'로 바꿔서 출력
# print(a.replace('makes', 'made'))
# # 6. 문자열 a를 대문자와 소문자로 변환하여 출력
# print(a.upper())
# print(a.lower())
# # 7. 문자열 a에서 양쪽 공백 삭제하기
# a = '    Practice makes perfect    '
# print(a.strip())

# a = ['b', 'a', 'n', 'a', 'n']

# ## 반환하지 않는 메서드(Void methods) -> 주로 원본을 변경한다
# # 1. 리스트의 마지막에 'a' 추가하기
# a.append('a')
# print(a)
# # 2-1. 리스트를 오름차순으로 정렬
# a = ['b', 'a', 'n', 'a', 'n']
# a.sort()
# print(a)
# # 2-2. 리스트를 내림차순으로 정렬
# a = ['b', 'a', 'n', 'a', 'n']
# a.sort(reverse=True)
# print(a)
# # 3. 리스트를 역순으로 뒤집기
# a = ['b', 'a', 'n', 'a', 'n']
# a.reverse()
# print(a)
# # 4. 리스트에서 문자 'a' 삭제하기
# a = ['b', 'a', 'n', 'a', 'n']
# a.remove('a')
# print(a)

# ## 반환하는 메서드(Return methods) -> 주로 원본을 변경하지 않는다.
# # 5. 리스트의 마지막 요소를 꺼내서 삭제하고 삭제한 요소 출력
# a = ['b', 'a', 'n', 'a', 'n']
# print(a.pop())
# # 6. 리스트에서 문자 'n'의 개수 출력
# a = ['b', 'a', 'n', 'a', 'n']
# print(a.count('n'))

'''
print('banana'.find('a')) # 1
print('banana'.find('z')) # -1
print('banana'.index('a')) # 1
# print('banana'.index('z')) # ValueError: substring not found

string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.islower()) # False
print(string2.islower()) # False

string1 = 'Hello'
string2 = '123'
print(string1.isalpha()) # True
print(string2.isalpha()) # False

print('Hello World'.istitle()) # True
print('Hello world'.istitle()) # False

text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python!

text = '    Hello, world!    '
new_text = text.strip()
print(new_text) # Hello, world!

text = 'Hello, world!'
words = text.split(',')
print(words) # ['Hello', ' world!']

words = ['Hello', ' world!']
text = '-'.join(words)
print(text) # Hello- world!

text = 'heLLo, woRld!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()
print(new_text1) # Hello, world!
print(new_text2) # Hello, World!
print(new_text3) # HELLO, WORLD!
print(new_text4) # HEllO, WOrLD!

text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')
print(new_text) #HEzzO, WOrLD!
'''

'''
mylist = [1, 2, 3]
mylist.append(4)
print(mylist) # [1, 2, 3, 4]

mylist = [1, 2, 3]
mylist.extend([4, 5, 6])
print(mylist) # [1, 2, 3, 4, 5, 6]

mylist = [1, 2, 3]
mylist.insert(1, 5)
print(mylist) # [1, 5, 2, 3]

mylist = [1, 2, 3]
mylist.remove(2)
print(mylist) # [1, 3]

mylist = [1, 2, 3, 4, 5]
item1 = mylist.pop()
item2 = mylist.pop(0)
print(item1) # 5
print(item2) # 1
print(mylist) # [2, 3, 4]

mylist = [1, 2, 3]
mylist.clear()
print(mylist) #[]

mylist = [1, 2, 3]
index = mylist.index(2)
print(index) # 1

mylist = [1, 2, 2, 3, 3, 3]
count = mylist.count(3)
print(count) # 3

mylist = [5, 4, 3, 2, 1]
mylist.sort()
print(mylist) # [1, 2, 3, 4, 5]
mylist.sort(reverse = True) # 내림차순
print(mylist) # [5, 4, 3, 2, 1]

mylist = [1, 3, 2, 8, 1, 9]
mylist.reverse()
print(mylist) # [9, 1, 8, 2, 3, 1]
'''