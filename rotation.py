import sys
sys.stdin = open("input.txt", "r")

T = int(input()) # 테스트 케이스의 개수

for test_case in range(1, T+1): # 테스트 개수만큼 반복
    N = int(input()) # N x N 행렬
    
    tlist = [] # 시작 리스트 생성
    for i in range(N):
        line = list(map(int, input().split())) # 행렬 입력받기
        tlist.append(line) # 리스트에 넣기
    
    rlist = [] # 최종 리스트
    for i in range(N): 
        rlist.append([]) # 빈 행렬
    
    def rotation(): # 회전 함수
        for i in range(N): # 가로축
            for j in range(N): # 세로축
                nlist[i][N-j-1] = tlist[j][i] # 회전
    
    for i in range(3):
        nlist = [] # 중간 리스트(회전 결과 저장)
        for x in range(N):
            nlist.append([])
            for y in range(N):
                nlist[x].append(0) # 0으로 가득찬 리스트
        
        rotation() #회전
        
        for k in range(N):
            rlist[k].append(nlist[k]) # 회전 결과를 최종리스트에 저장
        
        tlist = nlist # 시작 리스트에 회전 결과 할당
    
    print(f'#{test_case}', end = '\n')
    for x in range(N): # N번 반복
        for y in range(3): # 3번 회전이니까 3번
            p='' # empty str
            # for z in range(N): #
            #     p += str(rlist[x][y][z])
            for z in rlist[x][y]:
                p += str(z)
            rlist[x][y] = p
            print(rlist[x][y], sep = '', end = ' ')
        print()