'''
for i in range(1, 11, 1):
    print(i);
'''
'''
for i in range(0, 3, 1):
    print("i:",i,"Understanding the for command");
'''
'''
for i in range(1, 11, 1):
    if i % 2 == 0:
        print("i =",i,": Check value");
'''
'''
for i in range(1, 11, 2):
    print("i=",i,":Check value");
'''
'''
for i in range(10, -1, -1):
    print(i,":print 10 ~ 0");
'''
'''
i , sum = 0 , 0;
start , en , grow = 0 , 0 , 0;
start = int(input("Enter start value : "));
en = int(input("Enter end value : "));
grow = int(input("Enter condition value : "));
for i in range (start, en + 1, grow):
    sum = sum + i
print("The sum of values increased by %d from %d to %d : %d" %(grow, start, en, sum));
'''
'''
i, sum = 0, 0;
num = 0;
num = int(input("Enter value : "));
for i in range(num + 1):
    print(i);
    sum = sum + i
print("The Sum from 0 to %d : %d"%(num,sum));
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
    print("Enter",i,"into i and run print()");
    print(type(i));
'''
'''
#Example problem
#print multiple of 7 only
sta=int(input("Enter start value\t: "))
end=int(input("Enter end value\t: "))
grow=int(input("Enter condition value\t: "))
for i in range(sta,end+1,grow):
    if i % 7 == 0:
        print(i,end=" ")
'''
'''
#Example problem
#Sum of the multiples of 5 and multiples of 3 from 1 to 100
sum = 0
for i in range(1,101,1):
    if i%3==0 and i%5==0 :
        sum += i
print(sum)
'''
'''
for i in range(0, 3, 1):
    for k in range(0, 2, 1):
        print("Double for command(i:%d\tk:%d)"%(i,k));
'''
'''
#print 0 - 0 0 0 0 0, 1 - 0 1 2 3 4, 2 - 0 2 4 6 8, 3 - 0 3 6 9 12, 4 - 0 4 8 12 16
for i in range(0,5,1):
    print(i,"-",end=" ")
    for j in range(0,5,1):
        print(j*i,end=" ")
    print()
'''
'''
#Example Problem
#1 to 25 5 print per line
#ex)
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