# # 진법(n진수 -> 10진수)
# print(0b10)
# print(0o30)
# print(0x20)

# # 진법(10진수 -> n진수)
# print(bin(12))
# print(oct(12))
# print(hex(12))

# a = 3.2 - 3.1
# b = 1.2 - 1.1
# print(a)
# print(b)

# print(abs(a - b) <= 1e-10)

# import math
# print(math.isclose(a,b))

# print(314e-2)
# print(314 * 10 ** -2)

# li = [1, 2, 3, 4, 5, 6]
# print(len(li))
# print(type(li))

# print('줄바꿈 \n 탭 \t 백슬래시 \\ 작은따옴표 \' 큰따옴표 \"')

# bugs = 'roaches'
# counts = 13
# area = 'living room'

# # Debugging roaches 13 living room
# print('Debugging roaches 13 living room')
# print(f'Debugging {bugs} {counts} {area}')

# greeting = 'hi'
# print(f'{greeting:>10}')
# print(f'{greeting:^10}')
# print(f'{3.12319352352:.4f}')

# my_str = 'hello'

# # 인덱싱
# print(my_str[1])

# # 슬라이싱
# print(my_str[2:4])

# # 길이
# print(len(my_str))

# print(my_str[::-1])

# my_str[1] = 'z'

# my_list = [1, 2, 3, 'python', ['hello', 'world', '!!!']]
# print(len(my_list))
# print(my_list[4][-1])
# print(my_list[-1][1][0])

# my_list[0] = 100
# print(my_list)

# mytuple = (1,)
# print(mytuple)

# my_range_1 = range(5)
# my_range_2 = range(1,10)

# print(list(my_range_1))
# print(list(my_range_2))

# my_set_1 = {1, 2, 3}
# my_set_2 = {3, 6, 9}

# print(my_set_1 | my_set_2)
# print(my_set_1 - my_set_2)
# print(my_set_1 & my_set_2)

# list_1 = [1, 2, 3]
# list_2 = list_1

# list_1[0] = 100
# print(list_1)
# print(list_2)

# print('다음은 이형기 시인의 "낙화"의 한 구절이다.\n- 1연\n\t가야할 때 언제인가를\n\t분명히 알고 가는 이의\n\t뒷모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.')

# author_1 = '권필'
# author_2 = '허균'
# book_1 = '주생전'
# book_2 = '홍길동전'

# print(f'{book_1}의 작가는 {author_1}이고,')
# print(f'{author_2}은 {book_2}를 집필하였다.')

# books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
# authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

# print(authors[1],':',books[3])
# print(authors[3],':',books[1])
# print(authors[0],':',books[2])
# print(authors[2],':',books[0])
# print(authors[4],':',books[4])

# information = dict()
# authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
# books = [
#     ['장화홍련전', '가락국 신화', '온달 설화'],
#     ['금오신화', '이생규장전', '만복자서포기'],
#     ['수성지', '백호집', '원생몽유록'],
#     ['홍길동전', '장생전', '도문대작'],
#     ['옥루몽', '옥련몽'],
# ]

# '''
# - 작가와 작품 목록 참고
# - 허균 : 홍길동전, 장생전, 도문대작
# - 임제 : 수성지, 백호집, 원생몽유록
# - 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
# '''

# information[authors[0]] = books[1]
# information[authors[1]] = books[3]
# information[authors[2]] = books[4]
# information[authors[3]] = books[0]
# information[authors[4]] = books[2]

# for i in information.keys():
#     print(f'{i} : {information[i]}')

# print(3 + 5.0)
# print(True + 3)
# print(True + False)

# print(int(3.9))
# print(str(1) + 'st')

# vowels = 'aeiou'
# print(('a' and 'b') in vowels)
# print(('b' and 'a') in vowels)
# print(('a' in vowels and 'b' in vowels))
# print(('b' in vowels and 'a' in vowels))

# catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'], 
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'], 
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'], 
#     ['성공의 열쇠', '내면의 변화', '목표의 달성']
# ]

# backup_catalog = []
# for i in range(len(catalog)):
#     backup_catalog.append(catalog[i])

# ''' 
# 도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
# '성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
# '''
# catalog[3] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']

# print('catalog와 backup_catalog를 비교한 결과')
# print(catalog == backup_catalog) 
# print()

# print('backup_catalog : ')
# print(backup_catalog)
# print()

# print('catalog : ')
# print(catalog)

# book = '1'
# total = 10
# guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
# print(guide)
# print(int(book) * total)

# changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
# rental = 3.0
# print(changes)
# print(total - int(rental))

# authors = ['작자 미상', '이항복', '임제', '임제', 
#            '조성기', '조성기', '조성기', '임제', 
#            '허균', '허균', '허균', '임제', '임제', 
#            '임제', '임제', '임제', '임제', '임제', 
#            '임제', '임제', '임제', '박지원', '이항복', 
#            '남영로', '남영로', '남영로', '이항복', '임제', '임제']

# print(set(authors))

T = int(input()) # 테스트 케이스의 개수
for test_case in range(1, T+1): # 테스트 개수만큼 반복
    N = int(input()) # N x N 행렬
    tlist = [] # 빈 리스트 생성
    for i in range(N):
        line = list(map(int, input().split())) # 행렬 입력받기
        tlist.append(line) # 리스트에 넣기
    import copy
    oglist = copy.deepcopy(tlist)
    # for i in range(N):
    #     oglist.append(tlist[i])
    def rotation(): # 회전 함수
        for i in range(N): # 가로축
            for j in range(N): # 세로축
                tlist[i][N-j-1] = tlist[j][i] # 회전
                # tlist = []
                # tlist = oglist
            # tlist = oglist
    rotation()
    print(tlist)
    print(oglist)

