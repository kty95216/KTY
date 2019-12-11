'''
for i in range(1, 11, 1):
    print(i);
'''
'''
for i in range(0, 3, 1):
    print("i:",i,"for 문 이해하기^^");
'''
'''
for i in range(1, 11, 1):
    if i % 2 == 0:
        print("i =",i,": 값 확인");
'''
'''
for i in range(1, 11, 2):
    print("i=",i,":값 확인");
'''
'''
for i in range(10, -1, -1):
    print(i,":10 ~ 0 까지 출력");
'''
'''
i , sum = 0 , 0;
start , en , grow = 0 , 0 , 0;
start = int(input("시작값 입력 : "));
en = int(input("끝값 입력 : "));
grow = int(input("증감값 입력 : "));
for i in range (start, en + 1, grow):
    sum = sum + i
print("%d에서 %d까지 %d씩 증가한 값의 합 :%d" %(start, en, grow, sum));
'''
'''
i, sum = 0, 0;
num = 0;
num = int(input("값 입력 : "));
for i in range(num + 1):
    print(i);
    sum = sum + i
print("0에서 %d 까지 합 : %d"%(num,sum));
'''
'''
i=0;
for i in range(0,10):
    print(i);
'''
'''
i=10;
for i in range(10):
    print(i);
'''
'''
i=0;
for i in range(10,2):
    print(i);
'''
'''
i = 0
for i in range(0, 10, 2):
    print(i);
'''
'''
for i in [1,2,3,4,5,6,7,8,9,10]:
    print("i:",i);
'''
'''
list=[1,2,3,4,5,6,7,8,9,10];
for i in list:
    print("i:",i);
for i in list:
    print(i,end=" ");
'''
'''
st = "Hello Python";
for i in st:
    print("i:",i);
'''
'''
list = [10, "test", 123.123];
print("list:",list);
print();
for i in list:
    print("i에",i,"대입한 후 print() 실행");
    print(type(i));
'''
'''
#예시 코딩 문제 : 시작 값, 끝 값, 증가값(1) 입력받아 시작과 끝값 사이의 7의 배수를 출력하시오.
#결과는 1줄로 출력
start, en, grow = 0, 0, 0
start = int(input("시작값 입력 : "));
en = int(input("끝값 입력 : "));
grow = int(input("조건값 입력 : "));
for i in range(start, en+1, grow):
    if i % 7 == 0:
        print(i,end=" ");
'''
'''
#예시 코딩 문제 : 1 ~ 100 사이의 값 중 3의 배수 이며, 5의 배수에 해당하는 합을 구하시오.
sum=0;
for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 == 0:
        sum = sum + i;
print(sum);
'''
'''
for i in range(0, 3, 1):
    for k in range(0, 2, 1):
        print("이중 for문(i:%d\tk:%d"%(i,k));
'''
'''
#예시 코딩 문제 : 아래와 같이 출력하시오.
#상위포문 0 일때 하위 포문 : 0 0 0 0 0
#상위포문 1 일때 하위 포문 : 0 1 2 3 4
#상위포문 2 일때 하위 포문 : 0 2 4 6 8
#상위포문 3 일때 하위 포문 : 0 3 6 9 12
#상위포문 4 일때 하위 포문 : 0 4 8 12 16
for i in range(0, 5, 1):
    print("상위포문",i,"일때 하위 포문 :",end="");
    for k in range(0, 5, 1):
        print(i*k,end=" ");
    print();
'''
'''
#예시 코딩 문제 : 2중 for문을 이용하여 아래와 같이 출력 하시오.
#1	2	3	4	5
#6	7	8	9	10
#11	12	13	14	15
#16	17	18	19	20
#21	22	23	24	25
for i in range(1, 22, 5):
    print(i,end="\t");
    for k in range(i+1,i+5,1):
        print(k,end="\t");
    print();
'''