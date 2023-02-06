#체스 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수
Chess = list(map(int, input().split()))

# 맞는 개수 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
RightChess = [1, 1, 2, 2, 2, 8]

ans = []

for i in range(6):
    ans.append(RightChess[i] - Chess[i])

print(*ans)  #대괄호 없이 한 번에 출력