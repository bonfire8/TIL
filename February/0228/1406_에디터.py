import sys

Leftword = list(input())
M = int(input())
Rightword = []

for m in range(M):
    now = sys.stdin.readline().split()

    if now[0] == 'L':
        if Leftword == []:
            continue
        else:
            Rightword.append(Leftword.pop())
    elif now[0] == 'D':
        if Rightword == []:
            continue
        else:
            Leftword.append(Rightword.pop())
    elif now[0] == 'B':
        if Leftword == []:
            continue
        else:
            Leftword.pop()
    elif now[0] == 'P':
        Leftword.append(now[1])

print(''.join(Leftword), end='')
print(''.join(list(reversed(Rightword))), end='')