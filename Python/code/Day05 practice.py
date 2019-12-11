'''
#10 ~ 20 숫자를 입력 받아 1 부터 입력 받은 수 까지의 합 출력
num, result, i = 0, 0, 1
while True :
    num = int(input("10~20사이의 숫자 입력 : "))
    if num < 10 or num > 20 :
        print("잘못 입력 다시")
        continue
    break
while i <= num :
    result += i
    i += 1
else:
    print("1 ~",num,"까지의 합 : ",result)

# 다음 for문을 while문으로 변경
#for i in range(0, 3, 1):
#    for k in range(0, 5, 1):
#        if k == 3:
#            break
#        print("(i : %d\tk : %d)"%(i ,k))
i,k=0,0
while i < 3:
    k=0
    while k < 5:
        if k == 3:
            break
        print("(i : %d\tk : %d)"%(i, k))
        k+=1
    i+=1

# 쥐먹이문제
rice = 100000; mouse = 2; day=1;
while rice>0:
    rice -= mouse*20
    if day%10 == 0:
        mouse *= 2
    #print(day,"일차",mouse,"마리",rice,"그램")
    if rice <= 0:
        break
    day+=1
print(day,'일',mouse,'마리')

#자판기 문제
money, j = 0, 0;
money = int(input('요금을 투입 하세요 : '))
while True:
    print("==========커피 자판기==========")
    print("1. 커피(200)\t2. 코코아(250)\t3. 반환\t4. 종료")
    print("남은 금액 :",money)
    j = int(input("메뉴를 선택하세요 >>> "))
    if j == 4:
        break
    elif ((j == 1 and money < 200) or (j == 2 and money < 250)):
        print("요금이 부족합니다\n")
    elif j == 1:
        print("맛있게 드세요\n")
        money -= 200
    elif j == 2:
        print("맛있게 드세요\n")
        money -= 250
    elif j == 3:
        print("반환 금액 :",money,"\n")
        money = 0
    else:
        print("잘못입력하셨습니다\n")
print("프로그램 종료")
'''