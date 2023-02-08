N = int(input())
List = list(map(int, input().split()))
find = int(input())

#list  차례대로 돌려서 찾는 숫자와 같으면 1더하기
ans = 0
for i in range(N):
    if List[i] == find:
        ans += 1

print(ans)
