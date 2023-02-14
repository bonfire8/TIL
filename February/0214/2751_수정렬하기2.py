import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

#내장 함수 sort 사용
lst.sort()

for i in range(N):
    print(lst[i])