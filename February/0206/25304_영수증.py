TotalPrice = int(input()) #총금액
Num = int(input()) #물건들의 갯수

price = 0 #적혀있는 물건들의 총합
for i in range(Num):
    object, number = map(int, input().split())
    price += object * number

#총금액과 일치하면 Yes, 불일치하면 No
if TotalPrice == price:
    print('Yes')
else:
    print('No')