# number_of_people = 0

# def increase_user():
#     global number_of_people
#     number_of_people += 1

# result = []

# def create_user(**kwargs):
#     print(f'{kwargs["name"]}님 환영합니다 !')
#     return kwargs

# names = ['김시습', '허균', '남영로', '임제', '박지원']
# ages = [20, 16, 52, 36, 60]
# addresses = ['서울', '강릉', '조선', '나주', '한성부']

# result = list(map(lambda x: create_user(name = names[x], age = ages[x], address = addresses[x]), range(5)))

# print(result)

# # book.py
# number_of_book = 100

# def decrease_book(number):
#     global number_of_book
#     number_of_book -= number
#     print(f'남은 책의 수 : {number_of_book}')

# # ws_3_3.py
# def rental_book(name, number):
#     import book
#     book.decrease_book(number)
#     print(f'{name}님이 {number}권의 책을 대여하였습니다.')
# rental_book('홍길동', 3)

# # 실습 번호5.py
# number_of_people = 0

# def increase_user():
#     pass

# names = ['김시습', '허균', '남영로', '임제', '박지원']
# ages = [20, 16, 52, 36, 60]
# addresses = ['서울', '강릉', '조선', '나주', '한성부']

# def create_user(**kwargs):
#     print(f'{kwargs["name"]}님 환영합니다 !')
#     return kwargs

# many_user = list(map(lambda x: create_user(name = names[x], age = ages[x], address = addresses[x]), range(5)))

# def rental_book(name, age, address):
#     import book
#     book.decrease_book(age // 10)
#     print(f'{name}님이 {age // 10}권의 책을 대여하였습니다.')

# result = list(map(lambda x: rental_book(**many_user[x]), range(5)))

# list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

# rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

# everything = True

# for book in rental_book:
#     if book not in list_of_book:
#         print(f'{book} 은/는 보유하고 있지 않습니다.')
#         everything = False
#         break
# if everything:
#     print('모든 도서가 대여 가능한 상태입니다.')

list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

missing_book = [book for book in rental_book if book not in list_of_book]
if missing_book == []:
    print('모든 도서가 대여 가능한 상태입니다.')
else:
    for i in range(len(missing_book)):
        print(f'{missing_book[i]} 을/를 보충하여야 합니다.')