'''
tp = (10,20,30);
print("tp:",tp);
print("tp type:",type(tp));
print("tp len:",len(tp));
'''
'''
tp1 = 10,20,30;
print("tp1:",tp1);
print("tp1 type:",type(tp1));
print("tp1[0]type:",type(tp1[0]));
#tp1[0] = 100 #에러 발생 (내부 데이터 변경 불가능하기 때문에 오류)
'''
'''
tpType = "문자열",100,1.111;
print("tpType:",tpType);
print("type:",type(tpType));
print("tpType[0] type:",type(tpType[0]));
print("tpType[1] type:",type(tpType[1]));
print("tpType[2] type:",type(tpType[2]));
'''
'''
tpint = (10);
print("tpint:",type(tpint));
tpT1 = (10,);
print("tpT1:",type(tpT1));
tpT2 = 10,;
print("tpT2:",type(tpT2));
'''
'''
tt1 = (10,20,30,40);
tt2 = tt1[0]+tt1[1]+tt1[2]+tt1[3];
print("튜플 합:%d"%tt2);
print("tt1[1:3]:",tt1[1:3]);
print("tt1[1:]:",tt1[1:]);
print("tt1[:3]:",tt1[:3]);
'''
'''
a = 1,2,3;
b = 4,5,6;
c = a+b;
print("a:",a);
print("b:",b);
print("c:",c);
'''
'''
pack = 1,2,"패킹";
print("packing\npack:",pack);
a,b,c = pack;
print("unpacking\na:",a,"b:",b,"c:",c);
print("packing\npack:",pack);
a=10;
pack = a,b,c;
print("packing\npack:",pack);
'''
'''
tp = 100,200,"함수",100,"개수";
print("tp안의 200의 위치:",tp.index(200),"번째 인덱스");
print("tp안의 100의 개수:",tp.count(100),"개");
'''
'''
#예시 코딩 문제 : 여러 개의 값을 패킹시킨 후 저장되어 있는 값을 빼내어 출력 하시오
#(저장 되어 있는 값은 몇 개나 있는지 알 수 없는 상태이다)(5개 값 저장)
#튜플의 값을 리스트에 저장하시오
tp = 10,20,"test",3.3333,40;
ls = [];
for i in range(len(tp)):
    ls.append(tp[i]);
print("tp :",tp);
print("ls :",ls);
print(type(ls));
'''
'''
student = {"학번":1234 , "이름":"홍길동" , "학과":"it학과"};
print(student);
mobile = {"품명":"겔럭시" , "가격":100 , "크기":10};
print(mobile);
print(student["학번"]);
'''
'''
impo = {};
impo["파이썬"] = "www.python.org";
impo["네이버"] = "www.naver.com";
impo["구글"] = "www.google.com";
print("파이썬:",impo["파이썬"]);
print("네이버:",impo["네이버"]);
print("구글:",impo["구글"]);
print(impo);
'''
'''
impo = {};
name = input("키값 입력:");
val = input("값 입력:");
impo[name] = val;
print(name,":",impo[name]);
'''
'''
#예시 코딩 문제 : 하나의 대상을 선택하여 킷값과 값을 입력받아 저장 후 출력 하시오.
#이름(key) 입력:겐지
#값(value) 입력:수리검
#이름(key) 입력:맥크리
#값(value) 입력:섬광탄
#이름(key) 입력:파라
#값(value) 입력:로켓런처
#이름(key) 입력:리퍼
#값(value) 입력:샷건
#이름(key) 입력:솔저
#값(value) 입력:나선로켓
#{“솔저”:“나선로켓” , “맥크리”:“섬광탄” , “리퍼”:“샷건” , “파라”:“로켓런처” , “겐지”:“수리검”}
overwatch = {};
for i in range(0,5,1):
    name = input("이름(key) 입력:");
    val = input("값(value) 입력:");
    overwatch[name] = val;
print(overwatch);
'''
'''
num = {1:"일" , 2:"이" , 3:"삼" , 4:"사"};
print("keys()키:",num.keys());
print();
print("values()값:",num.values());
'''
'''
num = {1:"일" , 2:"이" , 3:"삼" , 4:"사"};
print("num.keys():",num.keys());
print("list(num):",list(num));
print("list(num.keys()):",list(num.keys()));
print();
print("num.values():",num.values());
print("list(num.values()):",list(num.values()));
'''
'''
singer = {};
singer["이름"]=input("가수 이름 입력:");
singer["구성원"]=input("인원수 입력:");
singer["대표곡"]=input("대표곡 입력:");
for i in singer.keys():
    print("%s:%s"%(i,singer[i]));
print(singer);
'''
'''
menu = {}; bl = True; num = 0;
while bl:
    print("1.메뉴 등록");
    print("2.메뉴별 가격 보기");
    print("3.가격 수정");
    print("4.종료");
    num = int(input(">>>"));
    if num == 1:
        name = input("메뉴 입력:");
        menu[name] = input("가격 입력:");
    elif num == 2:
        for i in menu.keys():
            print(i,":",menu[i]);
    elif num == 3:
        name = input("수정할 목록 입력:");
        menu[name] = input("수정가격:");
    elif num == 4:
        print("프로그램 종료 합니다");
        bl = False;
'''
'''
num = {1:"일" , 2:"이" , 3:"삼" , 4:"사" , 5:"오"};
print(num);
print("num.get(3):",num.get(3));    #밑에 #붙은코드와 똑같음
#print("num.get(3):",num[3]);
print("num.get(9):",num.get(9));
#print("num.get(9):",num[9]);
'''
'''
student = {"학번":1234 , "이름":"홍길동" , "학과":"it학과"};
print(student["학번"]);
print(student["이름"]);
print(student["학과"]);
print();
print(student.items());
print();
print(student);
'''
'''
name = {"이순신":"거북선" , "세종대왕":"훈민정음" , "파이썬":"프로그래밍 언어"};
for key,value in name.items():
    print(key,":",value);
print("삭제:",name.clear());
print("삭제 후 값:",name);
'''
'''
num = {1:"일" , 2:"이" , 3:"삼" , 4:"사" , 5:"오"};
print("변경전 값:",num);
print();
print("num.setdefault(9):",num.setdefault(9,"구~우"));
print();
print("변경전 후:",num);
print();
print("num.get(9)번째 value:",num.get(9));
'''
'''
dic = {};
ls = [];
ls.append(input("등록할 키값 입력:"));
ls.append(input("등록할 키값 입력:"));
ls.append(input("등록할 키값 입력:"));
dic = dic.fromkeys(ls);
print("dic키 설정:",dic);
dic=dic.fromkeys(ls,0);
print("dic 키&값 설정:",dic);
'''