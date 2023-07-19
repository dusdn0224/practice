import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
answer = list(range(1,10))
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sudoku = []
    for i in range(9):
        row = list(map(int, input().split()))
        sudoku.append(row)
    for a in range(9):
        sudoku[a].sort()
        if sudoku[a] != answer:
            print(f'#{test_case}', 0)
            break
    