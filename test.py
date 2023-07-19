# number_of_people = 0

# def increase_user():
#     global number_of_people
#     number_of_people += 1

# result = []

# def create_user(**kwargs):
#     global result
#     print(f'{kwargs["name"]}님 환영합니다 !')
#     result.append(kwargs)

# names = ['김시습', '허균', '남영로', '임제', '박지원']
# ages = [20, 16, 52, 36, 60]
# addresses = ['서울', '강릉', '조선', '나주', '한성부']

# create_user(name = names[0], age = ages[0], address = addresses[0])
# create_user(name = names[1], age = ages[1], address = addresses[1])
# create_user(name = names[2], age = ages[2], address = addresses[2])
# create_user(name = names[3], age = ages[3], address = addresses[3])
# create_user(name = names[4], age = ages[4], address = addresses[4])

# print(result)

# book.py
number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

# # ws_3_3.py
# def rental_book(name, number):
#     import book
#     book.decrease_book(number)
#     print(f'{name}님이 {number}권의 책을 대여하였습니다.')
# rental_book('홍길동', 3)

# 실습 번호5.py
number_of_people = 0

def increase_user():
    pass

names = ['김시습', '허균', '남영로', '임제', '박지원']
ages = [20, 16, 52, 36, 60]
addresses = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(**kwargs):
    global many_user
    print(f'{kwargs["name"]}님 환영합니다 !')
    many_user.append(kwargs)

many_user = []

create_user(name = names[0], age = ages[0], address = addresses[0])
create_user(name = names[1], age = ages[1], address = addresses[1])
create_user(name = names[2], age = ages[2], address = addresses[2])
create_user(name = names[3], age = ages[3], address = addresses[3])
create_user(name = names[4], age = ages[4], address = addresses[4])

print(many_user)

def rental_book(info):
    pass