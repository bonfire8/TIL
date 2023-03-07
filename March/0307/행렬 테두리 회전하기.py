def solution(rows, columns, queries):
    answer = []
    #1부터 들어가게 행렬 만들기
    array = [[columns * j + (i + 1) for i in range(columns)] for j in range(rows)]

    for query in queries:
        #1부터 시작하므로 -1 해주기
        a, b, c, d = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        #시계 방향으로 회전, 가로줄
        row1, row2 = array[a][b:d], array[c][b + 1:d + 1]
        minV = min(row1 + row2)

        #오른쪽 세로줄 아래쪽 값을 위쪽 값으로 위에서 아래로(시계방향) 한칸씩 이동
        for i in range(c, a, -1):
            array[i][d] = array[i - 1][d]
            #최소값 생기면 바꿔주기
            if array[i][d] < minV:
                minV = array[i][d]

        #왼쪽 세로줄 위쪽 값을 아래쪽 값으로 아래에서 위로(시계방향) 한칸씩 이동
        for i in range(a, c):
            array[i][b] = array[i + 1][b]
            #최소값 생기면 바꿔주기
            if array[i][b] < minV:
                minV = array[i][b]

        #가로줄 변경
        array[a][b + 1: d + 1], array[c][b:d] = row1, row2

        answer.append(minV)

    return answer