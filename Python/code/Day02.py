'''
print("정수 형 상수 사용 : %d"%300);
num=300
print("정수 형 변수 사용 : %d 입니다"%num);
print("정수 형 변수 사용 :",num,"입니다");
'''
'''
num=5
print("변경 전 num :",num);
num=num+10
print("변경 후 num :",num);
'''
'''
num1=5
num2=10
sum=num1+num2
print("두 수의 합 :",sum);
print("평균 값 :",sum/2);
'''
'''
num1=5
num2=10
sum = num1+num2
print("id num1 :",id(num1));    id명령어 : 변수 설정한 주소 값 불러옴
print("id num2 :",id(num2));
print("id sum :",id(sum));
'''
'''
num1 = 7;
num2 = 5;
sum = num1 + num2;
sub = num1 - num2;
mul = num1 * num2;
div = num1 / num2;
print("더하기\t:",sum);
print("빼기\t:",sub);
print("곱하기\t:",mul);
print("나누기\t:",div);
'''
'''
flt = 123.567
print("round(flt) :",round(flt));
print("round(flt,1) :",round(flt,1)); # %.1f
print("round(flt,2) :",round(flt,2)); # %.2f
'''
'''
flt = 123.123;
print("%.3f + %.3f = %.3f"%(flt,321.321,flt+321.321));
print(flt,"+",321.321,"=",flt+321.321);
ch1,ch2,ch3="파",'2',"썬";
print("%c + %c +%c = %s"%(ch1,ch2,ch3,ch1+ch2+ch3));
print(ch1,"+",ch2,"+",ch3,"=",ch1+ch2+ch3);
str_1 = "python";str_2="test";
str_3 = str_1 + str_2;
print("%s + %s = %s"%(str_1,str_2,str_1+str_2));
print(str_1,"+",str_2,"=",str_1+str_2);
'''
'''
num=100;
print("type : %s"%type(num));
flt = 321.321;
print("type : %s"%type(flt));
ch = "A";
print("type : %s"%type(ch));
st="test";
print("type : %s"%type(st));
ft = True;
print("type : %s"%type(ft));
'''
'''
num = 100;
print("type : %s\tid : %s"%(type(num),id(num)));
print("type : %s\tid : %s"%(type(num),id(num)));
num = 321.321;
print("type : %s\tid : %s"%(type(num),id(num)));
num = "A";
print("type : %s\tid : %s"%(type(num),id(num)));
num = "test"
print("type : %s\tid : %s"%(type(num),id(num)));
'''
'''
st1 = "Python";
st2 = "Test";
su = 100;
flt = 1.11;

num = '100';

print(flt+su);
print(st1 + st2);
#print(su+num)  # int형과 str형끼리 연산 불가
print(str(su)+num); #str(su): su숫자형을 str형으로 변경
print(su+int(num)); #int(num): num문자형을 int형으로 변경
'''
'''
su = 100;   #형변환 문제
print('type(su) :',type(su));
print('type(str(su)) :',type(str(su)));
print('type(float(su)) :',type(float(su)));
'''
'''
su = 100;       #int
num = '100';    #str
flt = "1.111";  #str
print(su+int(num));
print(float(num)+float(flt));
print(str(su)+num);
'''
'''
print("숫자 입력");
num1 = input();
print("입력 받은 값 :",num1);
'''
'''
print("두 수의 합을 구해 줍니다");
print("두 수 입력");
num1 = input();
num2 = input();
num3 = num1 + num2;
print("두 수의 합",num1,"+",num2,"=",num3);
print(type(num1), type(num2));  #input 명령어는 무조건 str형태로 입력받음
'''
'''
#input의 형변환
num1 = int(input());    #input의 str형태를 int형으로 형변환
num2 = int(input());    #input의 str형태를 int형으로 형변환

result = num1 + num2;
print(num1,"+",num2,"=",result);

result = num1 - num2;
print(num1,"-",num2,"=",result);

result = num1 * num2;
print(num1,"*",num2,"=",result);

result = num1 / num2
print(num1,"/",num2,"=",result);
'''
'''
#형변환 형태 확인
print("문자열 입력");
name = input();
print("정수 입력");
age = int(input());
print("실수 입력");
flt = float(input());

print("name 값:",name,"\t type:",type(name));
print("age 값:",age,"\t type:",type(age));
print("flt 값:",flt,"\t type:",type(flt));
'''
'''
name = input("이름을 입력 하세요:");
age = int(input("나이를 입력 하세요:"));
addr = input("주소를 입력 하세요:");
print("이름:",name,"\n나이:",age,"\n주소:",addr);
'''
'''
#input() 함수의 예시 코딩 문제
name = input("학생 이름 : ");
A = int(input("국어 점수 : "));
B = int(input("영어 점수 : "));
C = int(input("수학 점수 : "));
sum = A + B + C;
avr = round(sum/3,2);

print("====================학생 정보====================");
print("이름\t 국어\t 영어\t 수학\t 합계\t 평균\t");
print(name,"\t",A,"\t",B,"\t",C,"\t",sum,"\t",avr);
'''
'''
su1 = 3.1; su2 = 3;
print("su1>=su2:",(su1>=su2));
print("su1<=su2:",(su1<=su2));
print("su1==su2:",(su1==su2));
print("su1!=su2:",(su1!=su2));
'''
'''
su1=3.1; su2=3

print("su1 >= su2 : %d" % (su1 >= su2))
print("su1 <= su2 : %d" % (su1 <= su2))
print("su1 == su2 : %d" % (su1 == su2))
print("su1 != su2 : %d" % (su1 != su2))
'''
'''
su1 = su2 = 5;
su1+=1;
print("su1 + 1 =",su1);
su1-=1;
print("su1 - 1 =",su1);
su1*=su2;
print("su1 * su2 =",su1);
su1//=su2;
print("su1 // su2 =",su1);
su1%=su2;
print("su1 % su2 =",su1);
'''
'''
su1 = 5;
su2 = 3;
su1 **= su2;
su1 -= 2;
print("su1/4 =",su1/4);
print("su1//4 =",su1//4);
print("su1%4 =",su1%4);
'''
'''
print(0 or 0,":",False or False);
print(1 or 0,":",True or False);
print(0 or 1,":",False or True);
print(1 or 1,":",True or True);

print("not:",not(0 or 0),":",not(False or False));
print("not:",not(1 or 1),":",not(True or True));
'''
'''
print(0 and 0,":",False and False);
print(1 and 0,":",True and False);
print(0 and 1,":",False and True);
print(1 and 1,":",True and True);

print("not:",not 0,":",not False);
print("not:",not 1,":",not True);
'''
'''
num1 = 3;
num2 = 5;
result = num1 | num2; #3 : 011 , 5 : 101 --> 7 : 111
print(result);
'''
'''
num1 = 3;
num2 = 5;
result = num1 & num2; #3 : 011 , 5 : 101 --> 1 : 001
print(result);
'''
'''
num1 = 3;
num2 = 5;
result = num1 ^ num2 #xor : 입력 값 두개가 다른 경우에만 1 , 3 : 011 , 5 : 101 --> 6 : 110
print(result);
'''
'''
num1=8;
num2=num1>>2;
num3=num1<<2;
print(num1,"\t",num2,"\t",num3);  #1000     0010    00100000
'''
'''
print(1 in (1,2,3))
print(4 in (1,2,3))
print(4 not in (1,2,3))
print(1 not in (1,2,3))
'''
'''
print(type(1) is int)
print(type(1) is not int)
print(type('1') is not int)
'''