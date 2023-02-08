#1번부터 30번까지 학생명단
students = list(range(1, 31))

#28줄까지 반복문을 통해 제출한 번호가 학생명단안에 있으면 해당 번호를 삭제
for i in range(28):
    N = int(input())
    if N in students:
        students.remove(N)

#명단 최소, 최대순으로 출력
print(min(students))
print(max(students))
