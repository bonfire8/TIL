def solution(line):
    pos, answer = [], []
    n = len(line)

    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)

    for i in range(n):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]
            #평행, 일치인 경우 제외
            if a * d == b * c:
                continue
            #교점 구하기
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            #정수일때 pos에 추가
            if x == int(x) and y == int(y):
                pos.append([int(x), int(y)])
                #최소값, 최대값 변경
                if x_min > int(x):
                    x_min = int(x)
                if y_min > int(y):
                    y_min = int(y)
                if x_max < int(x):
                    x_max = int(x)
                if y_max < int(y):
                    y_max = int(y)
    #가장 작은 사각형 크기 구하기
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    #'.'으로 사각형 그리기
    coord = [['.'] * x_len for _ in range(y_len)]
    #범위 내일때 좌표 '*'로 변경
    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = '*'
    #문자열을 2~3개이상 합친다면 ''.join() 사용, + 사용하면 시간초과
    for result in coord:
        answer.append(''.join(result))
    #역순으로 출력
    return answer[::-1] # answer.reverse()