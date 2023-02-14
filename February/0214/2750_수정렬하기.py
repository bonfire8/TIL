N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

#버블정렬
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(N):
    print(lst[i])

#버블정렬 2
for i in range(N):
    for j in range(N):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in range(N):
    print(lst[i])
