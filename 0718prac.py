# decimal = 10
# # 1. 2진수로 출력해 보세요
# print(bin(decimal)[2:]) # 0b 없이 출력
# # 2. 2진수로 출력해 보세요
# print(oct(decimal)[2:]) # 0o 없이 출력
# # 3. 2진수로 출력해 보세요
# print(hex(decimal)[2:]) # 0x 없이 출력

# a = 3.2 - 3.1
# b = 1.2 - 1.1
# '''
# 부동 소수점 값을 출력할 때
# f-string을 활용하여
# 부동소수점의 정확도를 제어할 수 있다.
# '''
# print(f'a = {a:.1f}, b = {b:.1f}') # 소수점 첫번째 자리까지 출력

# print(314e-2)
# # 산술 연산자를 사용하여 표현식 바꾸기
# print(314 * 10 ** -2)

# greeting = 'hi'
# print(f'{greeting:>10}') # 오른쪽 정렬 ㅁㅁㅁㅁㅁㅁㅁㅁhi
# print(f'{greeting:^10}') # 가운데 정렬 ㅁㅁㅁㅁhiㅁㅁㅁㅁ
# print(f'{greeting:<10}') # 왼쪽 정렬   hiㅁㅁㅁㅁㅁㅁㅁㅁ

# greeting = 'hello world'
# # 1. 인덱싱 -> 알파벳 w 출력
# print(greeting[6])
# # 2-1. 슬라이싱 -> hello 출력
# print(greeting[:5])  # greeting[start:end:step]
# print(greeting[0:5]) # 1. step > 0 -> start 부터 end - 1 까지
#                      # 2. step < 0 -> start 부터 end + 1 까지
# # 2-2. 슬라이싱 -> world 출력
# print(greeting[6:])
# print(greeting[6:11])
# # 2-3. 슬라이싱 -> 거꾸로 출력
# print(greeting[::-1])
# # 3. 내장함수를 사용하여 문자열의 길이 출력
# print(len(greeting))
# # 4. for문을 활용하여 hello world 출력
# for i in greeting:
#     print(i, end = '')
# print()
# for i in range(len(greeting)):
#     print(greeting[i], end = '')

# array = [
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9]
# ]
# # 1. 인덱싱하여 3 출력
# print(array[0][2])
# # 2. 인덱싱하여 7 출력
# print(array[2][0])

# # 2차원 리스트를 입력받는 법
# rows = int(input('행의 개수를 입력하세요: '))
# # 방법 1
# matrix = []
# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# # 방법 2
# matrix = [list(map(int, input().split())) for _ in range(rows)]
# for row in matrix:
#     print(row)

# # 튜플 사용 예시
# def move_around(position):
#     x, y = position
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 상, 하, 좌, 우
#     directions_2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)] # 대각선

# # range -> 주로 반복문과 함께 쓰임
# # range(end): 0부터 end-1까지 1씩 증가
# range(3)
# for i in range(3): # 3번 반복하는 반복문
#     print()
# # range(start, end): start부터 end-1까지 1씩 증가
# range(2, 5)
# # range(start, end, step)
# # start < end: start부터 end-1까지 step만큼 증가
# # start > end: start부터 end+1까지 step만큼 감소
# range(1, 10, 2)
# for i in range(10, 0, -1):
#     print(i)

# my_dict = {
#     'a1': {'b1': 1, 'b2': 2, 'b3': 3},
#     'a2': {'b1': 4, 'b2': 5, 'b3': 6},
#     'a3': {'b1': 7, 'b2': 8, 'b3': 9}
# }
# # value 5 출력
# print(my_dict['a2']['b2'])
# print(my_dict.get('a2').get('b2'))

# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {4, 5, 6, 7, 8, 9}
# # 합집합
# print(set_1 | set_2)
# # 차집합
# print(set_1 - set_2)
# # 교집합
# print(set_1 & set_2)

# #세트의 사용 예시 -> 로또 번호 추첨
# import random # 모듈
# lotto = set() # 세트 생성
# while len(lotto) < 6: # 번호 6개가 나올 때까지
#     number = random.randint(1, 45) # 번호 뽑기
#     lotto.add(number) # 번호 추가하기
# lotto_list = list(lotto) # list로 형변환
# lotto_list.sort() # 오름차순 정렬
# print(lotto) # 번호 출력

# print(bool('')) # False
# print(bool(0)) # False
# print(bool(0.0)) #False
# # 나머진 다 True
# print(bool(' ')) # True
# print(bool('0')) # True
# print(bool('0.0')) # True

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print(total)
# print(sum(numbers))

# a = [3]
# b = [3]
# print(a == b)
# print(a is b)

# vowels = 'aeiou'
# print(('a' and 'b') in vowels)
# print(('b' and 'a') in vowels)
# print(3 and 5)
# print(3 and 0)
# print(0 and 3)
# print(0 and 0)
# print(5 or 3)
# print(3 or 0)
# print(0 or 3)
# print(0 or 0)
# print(('a' and 'b'))
# print(('b' and 'a'))

numbers = [1, 2, 3, 4, 5]
result = 4 not in numbers
print(result)
result = not (4 in numbers)
print(result)