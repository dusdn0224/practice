# number_of_people = 0


# def increase_user():
#     global number_of_people
#     number_of_people += 1


# increase_user()
# increase_user()
# print(number_of_people)

number_of_people = 0
print(f'현재 가입 된 유저 수 : {number_of_people}')

def increase_user():
    global number_of_people
    number_of_people += 1
    

def create_user(name, age, address):
    increase_user()
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다 !')
    print(user_info)

names = ['김시습', '허균', '남영로', '임제', '박지원']
ages = [20, 16, 52, 36, 60]
addresses = ['서울', '강릉', '조선', '나주', '한성부']
user_info = dict()
pair = zip(names, ages, addresses)
# for name, age, address in zip(names, ages, addresses):
