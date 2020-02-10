'''
a,b,c,d = 0,0,0,0;
sum = 0;
a = int(input("Enter first number:"));
b = int(input("Enter second number:"));
c = int(input("Enter third number:"));
d = int(input("Enter fourth number:"));
sum = a + b + c + d;
print("sum:%d"%sum);
'''
'''
ls = [10,20,30,40];Sum = 0;
print("ls:",ls);
print("ls[0]:%d"%ls[0]);
print("ls[1]:%d"%ls[1]);
print("ls[2]:%d"%ls[2]);
print("ls[3]:%d"%ls[3]);
Sum = ls[0]+ls[1]+ls[2]+ls[3];
print("Sum :",Sum);
'''
'''
#Inefficient list code
ls = [0,0,0,0]; Sum=0;
ls[0]=int(input("Enter first number:"));
ls[1]=int(input("Enter second number:"));
ls[2]=int(input("Enter third number:"));
ls[3]=int(input("Enter fourth number:"));
Sum=ls[0]+ls[1]+ls[2]+ls[3];
print("ls[0]:%d"%ls[0]);
print("ls[1]:%d"%ls[1]);
print("ls[2]:%d"%ls[2]);
print("ls[3]:%d"%ls[3]);
print("Sum of lists:%d"%Sum);
'''
'''
ls = [0,0,0,0]; Sum=0;
print("len(ls):",len(ls));
for i in range(len(ls)):
    ls[i]=int(input(str(i)+" Enter number:"));
    Sum += ls[i];
for i in range(len(ls)):
    print("ls[%d]:%d"%(i,ls[i]));
print("Sum of lists:%d"%Sum);
'''
'''
ls = [0,0,0,0];
Sum , i = 0 , 0;
while i<len(ls):
    ls[i]=int(input(str(i)+" Enter number:"));
    Sum += ls[i];
    i += 1;
else:
    i = 0;
while i<len(ls):
    print("ls[%d]:%d"%(i,ls[i]));
    i += 1;
print("Sum of lists:%d"%Sum);
'''
'''
ls = [10,20,30,40];
print("ls:",ls);
print("\nls[1:3] => ls[1]~[2]:%s"%ls[1:3]);
print("ls[0:3] => ls[0]~[2]:%s"%ls[0:3]);
print("ls[2:] => ls[2]~[end]:%s"%ls[2:]);
print("ls[:2] => ls[0]~[1]:%s"%ls[:2]);
'''
'''
ls = [0,1,2,3];
print(type(ls));
print(type(ls[1]));
print(type(ls[1:3]));
'''
'''
ls = [10,20,30,40];
arr = ls;
print("ls:",ls,"ls id:",id(ls));
print("arr:",arr,"arr id:",id(arr));
ls[0] = 0;
print("ls:",ls,"ls id:",id(ls));
print("arr:",arr,"arr id:",id(arr));
'''
'''
ls = [10,20,30,40];
arr = ls;
arr[2]=20000;
print("ls:",ls,"ls id:",id(ls));
print("arr:",arr,"arr id:",id(arr));
'''
'''
ls = [10,20,30,40];
arr = ls[:];
arr[2]=20000;
print("ls:",ls,"ls id:",id(ls));
print("arr:",arr,"arr id:",id(arr));
'''
'''
import copy
ls = [10,20,30,40];
arr = copy.deepcopy(ls);
arr[2]=20000;
print("ls:",ls,"ls id:",id(ls));
print("arr:",arr,"arr id:",id(arr));
'''
'''
ls = [10,20,30];
arr = [40,50,60];
print("ls:",ls);
print("arr:",arr);
Str=ls + arr;
print("ls + arr=>Str",Str);
string = ls * 3;
print("ls * 3 => string:",string);
'''
'''
ls = [10,20,30];
arr = [40,50,60];
print("ls:",ls);
print("arr:",arr);
Str=[0,0,0];
for i in range(len(Str)):
    Str[i] = ls[i] + arr[i];
print("ls + arr => Str:",Str);
string=[0,0,0];
for i in range(len(string)):
    string[i] = ls[i] * 3
print("ls * 3 => string:",string);
'''
'''
#Selection sort code
ls = [4,8,2,7,6];
i,j = 0,0;
print("Before sort",ls);
for i in range(4):
    for j in range(i+1,5):
        if ls[i] > ls[j]:
            ls[i],ls[j] = ls[j],ls[i]; #ls[i]와 ls[j]를 교환
print("After sort",ls);
'''
'''
jumSu = [82,85,76,79,96]
rank = [1,1,1,1,1]
i,j=0,0
for i in range(5):
    for j in range(5):
        if jumSu[i] < jumSu[j]:
            rank[i]+=1
i=0
print("Score\tRank")
while i<5:
    print(jumSu[i],"\t",rank[i])
    i+=1
'''
'''
ls = [10,20,30];
ls.append(1000);
for i in range(0,4):
    print("ls[%d]:%d"%(i,ls[i]));
print("Total number of lists:",len(ls));
print("ls:",ls);
ls=[];
print("ls after initializing:",ls);
'''
'''
ls = [];
for i in range(0,4):
    ls.append(0);
Sum = 0;
for i in range(0,len(ls)):
    ls[i] = int(input(str(i+1) + " Enter number:"));
    Sum += ls[i];
for i in range(0,len(ls)):
    print("Enter value ls[%d] : %d"%(i,ls[i]));
print("Sum:%d"%Sum);
'''
'''
bb = [10,20,30];
cc = ["Python","run","test"];
dd = [10,"test",1.123];
for i in range(0,len(bb)):
    print("bb[%d] : %s"%(i,bb[i]),end="=>");
    print("type : %s"%type(bb[i]));
print();
for i in range(0,len(cc)):
    print("cc[%d] : %s"%(i,cc[i]),end="=>");
    print("type : %s"%type(cc[i]));
print();
for i in range(0,len(dd)):
    print("dd[%d] : %s"%(i,dd[i]),end="=>");
    print("type : %s"%type(dd[i]));
'''
'''
List = [30,20,10];
print("Current list : %s"%List);

List.append(40);
print("List after attend(40) : %s"%List);

print("value extracted by pop() : %s"%List.pop());
print("List after pop() : %s"%List);

List.sort();
print("List after sort() : %s"%List);

List.reverse();
print("List after reverse() : %s"%List);
del(List[2]);
print("List after del() : %s"%List);
'''
'''
List = [30,20,10];
print("Current list : %s"%List);
print("Location of 10 value : %d"%List.index(10));

List.insert(2,200);
print("List after insert(2,200) : %s"%List);

List.remove(200);
print("List after remove(200) : %s"%List);

List.extend([555,666,555]);
print("List after extend([555,666,555]) : %s"%List);

print("555 value counts : %d"%List.count(555));
'''
'''
aa = [[1,2,3,4,],[5,6,7,8],[9,10,11,12]];
print("[0][0]",aa[0][0]);
print("[0][1]",aa[0][1]);
print("[0][2]",aa[0][2]);
print("[0][3]",aa[0][3]);
print("[1][0]",aa[1][0]);
print("[1][1]",aa[1][1]);
'''
'''
import random;
i=0
for i in range(5):
    print(i," ",random.random());
'''
'''
import random;
i = 0;
for i in range(5):
    print(i," ",int(random.random()*100));
'''
'''
import random;
i=0;
for i in range(5):
    print(i," ",random.randrange(1,10));
'''
'''
import random;
aa=[1,2,3,4,5];
print(random.choice(aa));
'''
'''
import random;
bb=random.sample(range(1,46),6);
print(bb);
'''