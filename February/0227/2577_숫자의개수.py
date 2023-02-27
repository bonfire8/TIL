A = int(input())
B = int(input())
C = int(input())
num = A * B * C
lst = list(str(num))
numlst = [0] * 10

for i in range(len(lst)):
    numlst[int(lst[i])] += 1

for i in range(len(numlst)):
    print(numlst[i])

#다른 방법 count 함수
for n in range(10):
    print(lst.count(str(n)))