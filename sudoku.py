import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
answer = list(range(1,10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sudoku = [] # 빈 리스트
    check = 0 # 오답 확인용
    for i in range(9): # 스도쿠 입력받기
        row = list(map(int, input().split()))
        sudoku.append(row)
    for a in range(9): # 행 1~9 체크
        new = [] # 체크용 리스트
        for b in range(9):
            new.append(sudoku[a][b])
        new.sort()
        if new != answer: # 오답일 시
            check +=1 # +1
    for a in range(9): # 열 1~9 체크
        new = [] # 체크용 리스트
        for b in range(9):
            new.append(sudoku[b][a])
        new.sort()
        if new != answer: # 오답일 시
            check +=1 # +1
    for a in list(range(9))[::3]: # 작은 네모 체크(0, 3, 6)
        for b in list(range(9))[::3]: # (0, 3, 6)
            new = [] # 체크용 리스트
            for c in range(3): # (0, 1, 2)
                for d in range(3): # (0, 1, 2)
                    new.append(sudoku[c+a][d+b])
            new.sort()
            if new != answer: # 오답일 시
                check += 1 # +1
    if check == 0: # 오답이 없었으면 check == 0
        print(f'#{test_case}', 1)
    else: # 오답이 있었으면 check != 0
        print(f'#{test_case}', 0)