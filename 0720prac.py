# # 실습1. 정수를 입력받아 짝수면 'EVEN' 출력, 홀수면 'ODD' 출력
# n = int(input('정수를 입력해주세요: '))
# if n % 2 == 0:
#     print('EVEN')
# else:
#     print('ODD')

# # 실습2. 윤년 판별하기, 윤년이면 'leap year', 아니면 'common year'
# # 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지면 안된다
# # 연도가 400으로 나누어 떨어지면 윤년
# year = int(input('연도를 입력해주세요: '))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('leap year')
#         else: print('common year')
#     else:
#         print('leap year')
# # or
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('leap year')
# else:
#     print('common year')

# 실습1. 구구단출력 (중첩 for문)
'''
<2단>
2 * 1 = 2
2 * 2 = 4
...
...
<9단>
...

'''
# for i in range(2,10):
#     print(f'<{i}단>')
#     for j in range(1,10):
#         print(f'{i} * {j} = {i * j:>2}')

# 실습2. 정수 n을 입력받아 n단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램 작성
'''
n: 5
*
**
***
****
*****
'''
# n = int(input('정수를 입력해주세요: '))
# for i in range(n+1):
#     print('*' * i)

# while문
'''
초기식
while 조건식:
    code...
    증감식
'''
# while 조건식이 참인 동안 반복하는 반복문
# 프로그램 종료 조건 만들어 주셔야 합니다.

# # 실습1. continue를 이용하여 1부터 10까지 정수 중 홀수만 출력하기
# n = 0
# while n < 10:
#     n += 1
#     if n % 2 == 0:
#         continue
#     else:
#         print(n)

# # 실습2. break를 이용하여 'Shall we close? (y/n)' 문구에 y를 입력해야
# #        반복문을 탈출하고 'The end'를 출력하는 프로그램 작성
# while True:
#     answer = input('Shall we close? (y/n) ')
#     if answer == 'y':
#         print('The end')
#         break
 
# # 실습3. 정수를 입력받아 그 정수가 몇 자릿수 숫자인지 알아내는 프로그램 작성
# n = int(input('정수를 입력해주세요: '))
# a = 0
# while n >= 1:
#     a += 1
#     n //= 10
# print(a)

# import math
# numbers = [1, 4, 9, 16, 25]
# sqrt_numbers = []
# for number in numbers:
#     sqrt_numbers.append(math.sqrt(number))
# print(sqrt_numbers)

# # 실습1. 91, 92, 93 line을 list comprehension으로
# sqrt_numbers_2 = [math.sqrt(number) for number in numbers]
# print(sqrt_numbers_2)

# # 실습2. if 추가, 짝수만 넣기
# sqrt_numbers_3 = [math.sqrt(number) for number in numbers if number % 2 == 0]
# print(sqrt_numbers_3)

# import requests

# black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']
# dummy_data = []
# censored_user_list = {}
# def create_user():
#     global censored_user_list
#     global namelist
#     # namelist = []
#     # namelist.append(parsed_data['name'])
#     # censored_user_list = {parsed_data["company"]["name"]: namelist}
#     for i in range(10):
#         namelist = []
#         namelist.append(dummy_data[i]['name'])
#         result = censorship(dummy_data[i]['company'])
#         if result:
#             censored_user_list[dummy_data[i]['company']] = namelist

# def censorship(company):
#     if company in black_list:
#         print(f'{company} 소속의 {namelist[0]} 은/는 등록할 수 없습니다.')
#         return False
#     else:
#         print('이상 없습니다.')
#         return True

# # 무작위 유저 정보 요청 경로
# # API_URL = 'https://jsonplaceholder.typicode.com/users/10'
# # API 요청
# for i in range(1, 11):
#     response = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}')
# # JSON -> dict 데이터 변환
#     parsed_data = response.json()
#     # create_user()
#     # print(censored_user_list)
#     # if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
#     #     dummy_data.append(dict(company = parsed_data['company']['name'], 
#     #                            lat = parsed_data['address']['geo']['lat'],
#     #                            lng = parsed_data['address']['geo']['lng'],
#     #                            name = parsed_data['name']))
#     dummy_data.append(dict(company = parsed_data['company']['name'],
#                            name = parsed_data['name']))
# create_user()
# # print(dummy_data)
# print(censored_user_list)

# 응답 데이터 출력
# print(response)
# 변환 데이터 출력
# print(parsed_data)
# 변환 데이터의 타입
# print(type(parsed_data))

# 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])
# print(parsed_data['company']['name'])

user_data = [
    {
        'blood_group': 'AB',
        'company': 'Stone Inc',
        'mail': 'ian17@yahoo.com',
        'name': 'Kathryn Jenkins',
        'website': [
            'https://www.boyd-herrera.com/',
            'https://watson.com/',
            'http://www.mitchell.com/',
            'http://irwin-cline.biz/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fleming Ltd',
        'mail': 'patricianelson@yahoo.com',
        'name': 'Angel Williamson',
        'website': [
            'https://wilson-johnson.com/',
            'https://santiago-hammond.com/',
            'https://morales.com/',
            'https://fry-fleming.com/',
        ],
    },
    {
        'blood_group': 'A+',
        'company': 'Scott PLC',
        'mail': 'lisajones@gmail.com',
        'name': 'Stephanie Herman MD',
        'website': ['https://www.boyer-stevens.org/', 'http://www.johnson.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Warren-Stewart',
        'mail': 'allisonjennifer@gmail.com',
        'name': 'Jon Martinez',
        'website': ['https://www.berg.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fisher Inc',
        'mail': 'mross@yahoo.com',
        'name': 'Justin Brown',
        'website': [
            'https://www.gray.com/',
            'https://jones.com/',
            'http://williams.biz/',
            'https://hammond.net/',
        ],
    },
    {
        'blood_group': 'B-',
        'company': 'Pearson Group',
        'mail': 'gravesbarbara@hotmail.com',
        'name': 'Bobby Patterson',
        'website': ['https://www.cunningham.biz/', 'https://johnson.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'White, Andrade and Howard',
        'mail': 'mcole@gmail.com',
        'name': 'Michelle Strickland',
        'website': ['http://www.rose-gomez.com/', 'https://reilly.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Young',
        'mail': 'tmorales@hotmail.com',
        'name': 'Stephanie Moore',
        'website': ['https://schmidt.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Brooks PLC',
        'mail': 'wellsmatthew@hotmail.com',
        'name': 'Dr. David Johnson',
        'website': [
            'http://ford-dean.com/',
            'http://www.petersen.com/',
            'https://thompson-cooley.info/',
            'http://ryan-gay.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Stewart Group',
        'mail': 'sean37@hotmail.com',
        'name': 'Veronica Webb',
        'website': ['http://www.holmes.info/', 'http://www.morris.biz/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Cabrera, Perry and Harris',
        'mail': 'bgonzales@yahoo.com',
        'name': 'Lisa Wilcox',
        'website': ['https://www.small.com/', 'http://martin-petersen.com/'],
    },
    {
        'blood_group': 'B+',
        'company': 'Thomas, Lozano and Lopez',
        'mail': 'bperry@yahoo.com',
        'name': 'Brian Simmons',
        'website': [
            'http://reid.com/',
            'http://www.roman-neal.biz/',
            'https://www.hoover.org/',
            'https://www.lynn.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Baker-Leach',
        'mail': 'johnlucas@yahoo.com',
        'name': 'Carlos Robinson',
        'website': ['https://martin.com/', 'http://montgomery-cline.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Higgins, Higgins and Garcia',
        'mail': 'chris66@gmail.com',
        'name': 'Gabriel Collins',
        'website': ['https://www.cole-pugh.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Tanner, Wheeler and Weaver',
        'mail': 'leonardtammy@gmail.com',
        'name': 'Christopher Cook',
        'website': [
            'https://www.myers-reynolds.com/',
            'https://dunlap-rogers.com/',
            'https://luna.net/',
            'http://smith-miller.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Schaefer-Hunter',
        'mail': 'nsummers@gmail.com',
        'name': 'Daniel Monroe',
        'website': [
            'https://cook.net/',
            'http://carpenter.com/',
            'http://morris-terrell.com/',
        ],
    },
    {
        'blood_group': 'B+',
        'company': 'Stephens Group',
        'mail': 'rolson@gmail.com',
        'name': 'Molly Parks',
        'website': [
            'https://wright-vincent.biz/',
            'http://www.cruz.com/',
            'http://olson.org/',
            'http://gomez.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Fitzgerald, Costa and Hobbs',
        'mail': 'jennifervang@hotmail.com',
        'name': 'Jill Patterson',
        'website': [
            'https://www.brewer.com/',
            'https://malone-murray.info/',
            'http://evans.com/',
            'https://ortiz.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Frazier Ltd',
        'mail': 'vsolis@hotmail.com',
        'name': 'Marie May',
        'website': [
            'http://pratt.info/',
            'http://www.ortega.com/',
            'http://www.smith.net/',
            'https://nichols.biz/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Rodriguez and Sons',
        'mail': 'michael09@yahoo.com',
        'name': 'Julia Gonzalez',
        'website': [
            'https://www.cantrell.com/',
            'https://www.smith.net/',
            'http://delgado.com/',
            'http://stevens.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Arnold',
        'mail': 'christopher79@hotmail.com',
        'name': 'David Garza',
        'website': ['https://price.net/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Butler-Hernandez',
        'mail': 'angiechoi@yahoo.com',
        'name': 'Leslie Kemp',
        'website': ['http://www.martin-thompson.org/', 'http://martin.org/'],
    },
    {
        'blood_group': 'A-',
        'company': 'Schneider-Hensley',
        'mail': 'cesarsantos@hotmail.com',
        'name': 'Brandon Peterson',
        'website': [
            'https://www.owens-gay.com/',
            'https://www.santiago.org/',
            'https://www.singleton.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Hunter, Alvarado and Stewart',
        'mail': 'thomas16@gmail.com',
        'name': 'Matthew Stanley',
        'website': ['https://nelson.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Elliott, Mullins and Michael',
        'mail': 'smithedward@hotmail.com',
        'name': 'Robert Brown',
        'website': ['http://montgomery-rogers.biz/', 'http://www.williams-nixon.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Velasquez-Garcia',
        'mail': 'samanthawilson@yahoo.com',
        'name': 'Stephanie Cohen',
        'website': ['http://jackson-harris.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Mccoy-Hopkins',
        'mail': 'lli@yahoo.com',
        'name': 'Michael Clark',
        'website': [
            'https://www.harding.info/',
            'https://www.jones.biz/',
            'http://knight-adkins.org/',
            'http://www.alvarado-mendoza.org/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Kerr Ltd',
        'mail': 'georgebrittany@yahoo.com',
        'name': 'Brandon White',
        'website': ['https://flowers-parker.info/', 'http://oliver-rice.info/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Villarreal, Wood and Smith',
        'mail': 'denise73@yahoo.com',
        'name': 'Kevin Blevins',
        'website': [
            'http://www.ramirez.info/',
            'https://mckay.net/',
            'http://duran.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Jenkins-Garcia',
        'mail': 'kwoodward@hotmail.com',
        'name': 'Michelle Dixon',
        'website': [
            'http://www.taylor.com/',
            'https://bates-trujillo.org/',
            'https://www.thomas-boyer.org/',
        ],
    },
]

blood_types = ['A-', 'A+', 'B-', 'B+', 'O-', 'O+', 'AB-', 'AB+']
black_list = ['Jenkins-Garcia', 'Stephens Group', 'White, Andrade and Howard', 'Warren-Stewart']

def is_validation(data):
    # for i in range(len(data)):
    check = 0
    Falselist = []
    if data['company'] in black_list:
        return 'blocked'
    if data['blood_group'] not in blood_types:
        check += 1
        Falselist.append('blood_group')
    if '@' not in data['mail']:
        check += 1
        Falselist.append('mail')
    if 2 > len(data['name']) or len(data['name']) > 30:
        check += 1
        Falselist.append('name')
    if len(data['website']) < 1:
        check += 1
        Falselist.append('website')
    if check == 0:
        return True
    else:
        return False, Falselist

user_list = []
n = 0

def create_user(list):
    global user_list, n
    result = is_validation(list)
    if result == True:
        user_list.append(list)
    elif 'False' in str(result[0]):
        n += 1
        for i in range(len(result[1])):
            list[result[1][i]] = None
        user_list.append(list)
    else:
        n += 1

for i in range(len(user_data)):
    create_user(user_data[i])

print(f"'잘못된 데이터로 구성된 유저의 수는 {n} 입니다.'")
for i in range(len(user_list)):
    print(user_list[i])