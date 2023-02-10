N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    #가로줄마다 더해주고 한줄씩 출력
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    print(*row)