lst = list(input())

# 아스키 코드 변환
#문자열을 아스키코드로 ord()
#아스키코드를 문자열로 chr()

alpabet = [0] * 26

for i in range(len(lst)):
    alpabet[ord(lst[i])-97] += 1

print(*alpabet)

