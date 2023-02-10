ARR = []

for _ in range(9):
    ARR.append(list(map(int, input().split())))

#0부터 숫자가 있으므로 이보다 작은수인 -1을 첫번째 최댓값으로 설정
Max = -1
ansIndex = []

for i in range(9):
    for j in range(9):
        if Max < ARR[i][j]:
            Max = ARR[i][j]
            ansIndex=[i+1, j+1]

print(Max)
print(*ansIndex)