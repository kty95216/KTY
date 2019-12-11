'''
i = 0;
while i < 5:
    print(i,"종속 문장");
    i += 1;

print("다음 문장");
'''
'''
i = 1;
odd, even = 0,0;
while i <= 10:
    if i % 2 == 0:
        even += i;
    else:
        odd += i;
    i += 1;
print("1-10 짝수의 합 :",even);
print("1-10 홀수의 합 :",odd);
'''
'''
#while문을 for문으로 바꾸면
i , odd , even =0,0,0;
for i in range(1, 11, 1):
    if i % 2 == 0:
        even += i;
    else:
        odd += i;
print("1-10 짝수의 합 :",even);
print("1-10 홀수의 합 :",odd);
'''
'''
i = 0;
while i < 5:
    print(i, "종속 문장");
    i += 1;
else:
    print("조건식이 거짓일 경우 :",i);
print("다음 문장");
'''
'''
i = 1;
while True:
    print(i,"종속 문장",end=" ");
    i += 1 ;
'''
'''
i = 1;
flag = True
while flag:
    print(i,"종속 문장",end=" ");
    if i == 10:
        flag = True-1;
    i += 1;
'''
'''
i = 0;
while True:
    if i == 3:
        break
        print("3----출력");
    print(i,"출력");
    i += 1;
print("다음 문장");
'''
'''
i = 0;
while i < 5:
    i += 1;
    if i == 3:
        continue
        print("3----출력");
    print(i,"출력");
print("다음 문장");
'''
'''
num, result, i = 0, 0, 1;
while True:
    num = int(input("1~10사이의 숫자 입력:"));
    if num < 1 or num > 10:
        print("잘못 입력 다시");
        continue;
    break
else:
    print("next...");
while i <= num :
    result += i;
    i += 1;
else:
    print("1~",num,"까지의 합:",result);
'''
'''
#예시 코딩 문제
num, result, i = 0, 0, 1;
aaa = True;
while aaa:
    num = int(input("1~10사이의 숫자 입력:"));
    if num < 1 or num > 10:
        print("잘못 입력 다시");
        continue;
    aaa = False;
else:
    print("next...");
while i <= num :
    result += i;
    i += 1;
else:
    print("1~",num,"까지의 합:",result);
'''
'''
#예시 코딩 문제 : 10~20 사이의 숫자만 입력 받아 1부터 입력 받은 수까지의 합을 구하시오.
num, result, i = 0, 0, 1;
while True:
    num = int(input("10 ~ 20 숫자 입력 :"));
    if num < 10 or num > 20:
        print("다시 입력 하십시오");
        continue;
    break
while i <= num:
    result += i;
    i += 1;
else:
    print("1 ~",num,"까지의 합 :",result);
'''
'''
#예시 코딩 문제 : for I in range(0, 3, 1):
#			for k in range(0, 5, 1):
#				if k == 3:
#					break;
#				print(“(i : %d\tk : %d)”%(i, k));
#(i : 0	k : 0)
#(i : 0	k : 1)
#(i : 0	k : 2)
#(i : 1	k : 0)
#(i : 1	k : 1)
#(i : 1	k : 2)
#(i : 2	k : 0)
#(i : 2	k : 1)
#(i : 2	k : 2)	<-- 위의 for문을 while문으로 바꿔서 옆에와 같이 출력 되게 하시오.
i , k = 0 , 0;
while i <= 2:
    k = 0;
    while k <= 2:
        print("(i : %d\tk : %d)"%(i,k));
        k += 1;
    i += 1;
'''
'''
#예시 코딩 문제 : 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다.
#쥐 한 마리가 하루에 20g씩의 쌀을 먹고, 10일(10,20,30)마다 쥐의 수가 2배씩 증가한다.
#며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까? 그리고 쥐는 총 몇 마리 인가?
#(쌀 한 통 = 1kg)(쌀을 먹은 후 2배 증가하는 조건)
rice = 100000;
mouse = 2;
mouseday = mouse * 20;
day = 1;
while mouseday <= rice:
    day += 1;
    mouseday += mouse * 20;
    if day % 10 == 0:
        mouse = mouse * 2;
print(day,"일 안에",mouse,"마리");
'''
#예시 코딩 문제 : 요금을 투입 하세요
#		        >
#		        ==========커피 자판기==========
#		        1. 커피<200>	2. 코코아<250>	3. 반환	4. 종료
#		        메뉴를 선택하세요
#	        	>
#이렇게 만들기
money=int(input("요금을 투입하세요:"));
print("==========커피 자판기==========");
print("1. 커피<200>\t2. 코코아<250>\t3. 반환\t4. 종료");
a , b , c , d, amoney , bmoney = 0 , 0 , 0 , 0 , 0 , 0;
while True:
    menu=int(input("메뉴를 선택하세요:"));
    if menu == 1:
        a += 1;
        amoney += 200;
        c = money - a * 200;
        print("커피",a,"잔",amoney,"원 입니다");
        print("잔액",c,"원 입니다");
        if c < 0:
            print("요금이 부족합니다");
    if menu == 2:
        b += 1;
        amoney += 250;
        c = money - b * 250;
        print("코코아",b,"잔",amoney,"원 입니다");
        print("잔액",c,"원 입니다");
        if d < 0:
            print("요금이 부족합니다");