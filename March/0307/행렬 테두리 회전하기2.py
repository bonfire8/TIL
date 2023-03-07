def rotate(x1, y1, x2, y2, array):
    #첫값 밀려나서 사라지므로 기억해놓기
    first = array[x1][y1]
    minV = first

    #왼쪽 세로줄 아래에서 위로 이동
    for k in range(x1, x2):
        array[k][y1] = array[k + 1][y1]
        minV = min(minV, array[k + 1][y1])

    #아래쪽 가로줄 오른쪽에서 왼쪽으로(시계방향) 이동
    for k in range(y1, y2):
        array[x2][k] = array[x2][k + 1]
        minV = min(minV, array[x2][k + 1])

    #오른쪽 세로줄 위에서 아래로 이동
    for k in range(x2, x1, -1):
        array[k][y2] = array[k - 1][y2]
        minV = min(minV, array[k - 1][y2])

    #위쪽 가로줄 왼쪽에서 오른쪽으로 이동
    for k in range(y2, y1 + 1, -1):
        array[x1][k] = array[x1][k - 1]
        minV = min(minV, array[x1][k - 1])

    #첫번째 값 넣어주기
    array[x1][y1 + 1] = first
    return minV


def solution(rows, columns, queries):
    array = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, array))

    return result