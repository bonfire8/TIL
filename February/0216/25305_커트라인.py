N, k = map(int, input().split())
lst = list(map(int, input().split()))

#버블 정렬
for i in range(N-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst[N-k])