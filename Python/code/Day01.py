'''
print("반가워요~~ 파이썬 ^^"); print("hello")
print('Python 첫날 입니다'); print("Python을 시작해 볼까요")
'''
'''
print("Hello \"주말\" Python");
print("Hello \nPython");
print("쒼나는");print("Python")
'''
'''
print("Hello"
" Python"
" Start")
print("Hello\n"
"Python\n"
"Start")
'''
'''
예제
print("저의 이름은 김태영 입니다\n저의 나이는 24살 입니다\n주소는 안양시 입니다");
print("저의 이름은 김태영 입니다\n"
"저의 나이는 24살 입니다\n"
"주소는 안양시 입니다");
'''
'''
print("Have\t"
"a\t"
"Good\t"
"Time.");
print("1234567\t"
"1\t"
"12345678\t"
"123");
'''
'''
print("큰 따옴표 \"");
print("작은 따옴표 '");
print('큰 따옴표 "');
print('작은 따옴표 \'');
'''
'''
print('표현 \ 방식');
print('표현 \2 방식');
print('표현 \\2 방식');
#print('표현 방식\') #error code
print('표현 방식\\');
'''
'''
print("123 + 123");
print(542 - 242);
print(2 * 123);
print(120 / 3);
'''
'''
print("덧셈 결과 : ",123 + 123);
print("뺄셈 결과 : ",542 - 242);
print("곱셈 결과 :",2 * 123)
print("나눗셈 결과 : ",123 / 3);
'''
'''
print(125);
print(0b1111101);
print(0o175);
print(0x7D);
'''
'''
print(125);
print(bin(125));
print(oct(125));
print(hex(125));
'''
'''
print("2진수 :",bin(0b01111011));
print("8진수 :",oct(0b01111011));
print("16진수 :",hex(0b01111011));
print("10진수 :",0b01111011);
'''
'''
print("%d"%123);
#print("%d %d" % 123); #에러
#print("%d" % (123 , 321)); #에러
print("%d %d"%(123 , 321));
print("%d + %d = %d"%(123 , 321 , 123 + 321));
'''
'''
print("10진 정수 : %d"%123);
print("10진 정수 : %d"%0o173);
print("10진 정수 : %d"%0x7b);

print("8진 정수 : %o"%123);
print("8진 정수 : %o"%0o173);
print("8진 정수 : %o"%0x7b);

print("16진 정수 : %x"%123);
print("16진 정수 : %x"%0o173);
print("16진 정수 : %x"%0x7b);
'''
'''
print("정수 표현 : %d"%123);
print("정수 표현 : %d"%123.623);
print("정수 표현 : %d %d"%(123,456));

print("\n실수 표현 : %f"%456);
print("실수 표현 : %.2f"%456.456);
print("실수 표현 : %f %f"%(456.456 , 123.123));
'''
'''
print("문자 표현 : %c %c"%("한","글"));
print("문자 표현 : %c %c"%('표','현'));

print("\n문자열 표현 : %s"%"안녕");
print("문자열 표현 : %s\t%s"%('문자열',"표현방식"));
'''
'''
print("기본 값 : %d"%123);
print("설정 값 : %5d"%123);
print("설정 값 : %05d"%123);
print("설정 값 : %5d%5d"%(123,123));
print("설정 값 : %-5d%-5d"%(123,123));
'''
'''
print("기본 값 : %f"%123.45678);
print("설정 값 : %10.3f"%123.45678);
print("설정 값 : %2.1f"%123.45678);
print("설정 값 : %.2f"%123.45678);
'''
'''
print("기본 값 : %s"%"python test");
print("설정 값 : %20s"%"python test");
'''
'''
print('%s님의 나이는 %d 입니다.'%('김동환',38));
print('{}님의 나이는 {} 입니다.'.format('김동완',38));
'''
'''
print("%10s , %-10s"%('오른쪽','왼쪽'));
print("{:>10} , {:<10}".format('오른쪽','왼쪽'));
print('{:^10}'.format('가운데'));
'''
'''
print('{:,}'.format(1000000));
'''