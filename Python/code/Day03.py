'''
num1 = 10;
num2 = 15;
if num1 > num2:
    print("num1이 num2보다 크다");
'''
'''
num1 = int(input("수 입력:"));
if num1 % 2 == 0:
    print("num1 : ",num1,"짝수다");
print("나는 다음 문장");
'''
'''
num1 = int(input("수 입력:"));
if num1 % 2 == 0:
    print("num1 :",num1,"짝수다");
    print("num1 :",num1,"2의 배수이다");
print("나는 다음 문장");
'''
'''
print("1.easy game");
print("2.hard game");
print("3.exit");
num1 = int(input("선택 : "));
if num1 == 1:
    print("easy game start");
if num1 == 2:
    print("hard game star");
if num1 == 3:
    print("game exit");
'''
'''
#if문 문제 : 날짜를 입력받아 요일을 구하시오
#(단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 다시 월요일)
#(어떤 값을 입력을 받던 요일이 정확히 출력 되게 만드시오);
num1 = int(input("날짜 입력 : "));
if num1 % 7 == 1:
    print("월요일 입니다");
if num1 % 7 == 2:
    print("화요일 입니다");
if num1 % 7 == 3:
    print("수요일 입니다");
if num1 % 7 == 4:
    print("목요일 입니다");
if num1 % 7 == 5:
    print("금요일 입니다");
if num1 % 7 == 6:
    print("토요일 입니다");
if num1 % 7 == 0:
    print("일요일 입니다");
'''
'''
num = int(input("수 입력 : "));
if num == 1:
    print("1입력");
else:
    print("1이 아닌 값 입력");
'''
'''
arr = [1,2,3,4,5]; # 학습하지 않은 내용 : 리스트 C언어의 배열과 같음
na = int(input("찾을 숫자 입력 : "));
if na in arr:
    print("arr : ",arr,"찾는 숫자가 존재 합니다 : ",na);
else:
    print("arr : ",arr,"안에는 찾고자 하는 숫자가 없습니다 : ",na);
print("결과 :",na in arr);
'''
'''
st = "Hello Python Fun";
na = input("찾고자 하는 문자열 입력 : ");
if na in st:
    print("st:",st,"찾는 문자열:",na,"존재 한다");
else:
    print("st 안에는",na,"존재 하지 않습니다");
'''
'''
old_id = input("저장할 ID 입력 : ");
print("인증 프로그램 입니다");
print("ID와 PW를 입력하세요");
new_id = input("ID 입력 : ");
if old_id == new_id:
    print("인증 통과 했습니다");
else:
    print("인증 실패");
'''
'''
num = int(input("수 입력 : "));
if num % 3 == 0:
    if num % 2 == 0:
        print("num은 3의 배수이면서 짝수 입니다");
print("다음문장 실행");
'''
'''
num = int(input("수 입력 : "));
if num > 0:
    if num % 2 == 0:
        print("num은 양의 짝수 입니다");
    else:
        print("num은 양의 홀수 입니다");
else:
    print("num은 음수 입니다");
print("다음문장 실행");
'''
'''
num = int(input("수 입력 : "));
if num > 0:
    print("0보다 큰 수 입력");
elif num < 0:
    print("0보다 작은 수 입력");
else:
    print("0과 같은 수 입력");
'''
'''
#예시 코딩 문제 : 이름, 학번, 3과목의 성적을 입력 받아 합계와 평균을 구하고
#평균이 90이상이면 “A”, 80 이상“B”, 70이상 “C”, 60이상 “D”, 60미만이면 “F”를 출력하시오
name = input("이름 : ");
number = (input("학번 : "));
su1 = int(input("국어 점수 : "));
su2 = int(input("수학 점수 : "));
su3 = int(input("영어 점수 : "));
sum = su1 + su2 + su3;
avr = round(sum/3,2);
print("=============== 결과 출력 ================");
print("이름 :",name);
print("학번 :",number);
print("국어 점수 :",su1);
print("수학 점수 :",su2);
print("영어 점수 :",su3);
print("합계 :",sum);
print("평균 :",avr);
if avr >= 90:
    print("학점 : A");
elif avr >= 80:
    print("학점 : B");
elif avr >= 70:
    print("학점 : C");
elif avr >= 60:
    print("학점 : D");
else:
    print("학점 : F");
'''
'''
#예시 코딩 문제 : 커피의 개당 가격은 2000원이다. 10개 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다.
#커피의 개수를 입력 받아 금액을 출력하시오.
cnt = int(input("커피 잔 수?"));
if cnt <= 10:
    prize1 = cnt * 2000;
    print("커피 잔 수 :",cnt);
    print("커피 가격 :",prize1);
else:
    prize2 = 2000 * 10;
    prize3 = (cnt - 10) * 1500;
    print("커피 잔 수 :",cnt);
    print("커피 가격 :",prize2 + prize3);
'''
'''
#정수를 입력받아 아래와 같이 출력하시오.
#3의배수이면서, 4의배수입니다.
#3의배수 입니다.
#4의배수 입니다.
#3의배수도, 4의배수도 아닙니다.
#0은 3의 배수도 4의 배수도 아닙니다.
a = int(input("정수를 입력하세요 : "));
if a == 0:
    print("0은 3의 배수도 4의 배수도 아닙니다.");
elif a % 3 == 0:
    if a % 4 == 0:
        print("3의배수이면서, 4의배수 입니다");
    else:
        print("3의배수 입니다");
elif a % 4 == 0:
    print("4의배수 입니다");
else:
    print("3의배수도, 4의배수도 아닙니다");
'''
'''
#비행기를 타는데 30분 거리까지만 기본 요금은 30000원이며, 10분 단위로 추가요금 5000원씩 부가된다.
#비행기 탈 시간을 입력하여 요금 계산기를 만드시오.
money=30000;
time = int(input("비행기 탄 시간(분): "))
time-=30
if time > 9:
    money=money+time//10*5000
print(money,"원 입니다.")
'''