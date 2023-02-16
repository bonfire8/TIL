import math

lst = []
for _ in range(5):
    lst.append(int(input()))

#소수점 버리기
print(math.trunc(sum(lst)/5))

#버블정렬
for i in range(4, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst[2])