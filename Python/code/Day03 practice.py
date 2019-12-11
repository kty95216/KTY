'''
#이름, 학번, 점수3개 입력 > 이름, 학번, 평균, 학점출력
#학점은 90이상 A, 80이상 B, 70이상 C, 60이상 D, 나머지 F
name = input("이름 입력 : ")
num = input("학번 입력 : ")
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
sum = kor+eng+math
avg = round(sum/3,2)
print("=========== 결과 출력 ===========")
print("이름 :",name)
print("학번 :",num)
print("평균 :",avg)
if avg >= 90:
    print("학점 : A")
elif avg >= 80:
    print("학점 : B")
elif avg >= 70:
    print("학점 : C")
elif avg >= 60:
    print("학점 : D")
else:
    print("학점 : F")
#커피 1잔 2000원, 10잔 넘어가면 초과분에 대해서만 1500원
cnt=int(input("커피 몇 잔? "))
if cnt <= 10:
    prize=cnt*2000
    print("총 금액은",prize,"원 입니다.")
else:
    prize1 = 10*2000
    prize2 = (cnt-10)*1500
    print("총 금액은",prize1+prize2,"원 입니다.")
num = int(input('정수 입력 : '))
# 3번
if num==0: 
	print(num,"은(는) 3의 배수도 4의 배수도 아닙니다");
elif num%3==0 and num%4==0: 
	print(num,"은(는)3의 배수 이면서,4의 배수입니다");
elif num%3==0:
	print(num,"은(는)3의 배수 입니다");
elif num%4==0:
	print(num,"은(는)4의 배수 입니다");
else: 
	print(num,"는 3의 배수도 4의 배수도 아님");
#4번
money=30000;
time = int(input("비행기 탄 시간(분): "))
time-=30
if time > 9:
    money=money+time//10*5000
print(money,"원 입니다.")
'''