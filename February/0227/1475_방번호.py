N = list(input())

lst = [0] * 10

for i in range(len(N)):
    if int(N[i]) == 9:
        lst[6] += 1
    else:
        lst[int(N[i])] += 1

if lst[6] % 2 == 0:
    lst[6] = lst[6] // 2
else:
    lst[6] = lst[6] // 2 + 1

print(max(lst))
