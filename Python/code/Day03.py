'''
num1 = 10;
num2 = 15;
if num1 > num2:
    print("Number 1 is larger than number 2.");
'''
'''
num1 = int(input("Enter num1:"));
if num1 % 2 == 0:
    print("num1 : ",num1,"is even.");
print("I am the next sentence.");
'''
'''
num1 = int(input("Enter num1:"));
if num1 % 2 == 0:
    print("num1 :",num1,"is even.");
    print("num1 :",num1,"is a multiple of two.");
print("I am the next sentence.");
'''
'''
print("1.easy game");
print("2.hard game");
print("3.exit");
num1 = int(input("select : "));
if num1 == 1:
    print("easy game start");
if num1 == 2:
    print("hard game star");
if num1 == 3:
    print("game exit");
'''
'''
#Example problem(if) : Enter a date and find the day
#(However, the first day is definitely Monday. Sunday the 7th and Monday the 8th.)
num1 = int(input("Enter Date : "));
if num1 % 7 == 1:
    print("It’s Monday.");
if num1 % 7 == 2:
    print("It's Tuesday.");
if num1 % 7 == 3:
    print("It's Wednesday.");
if num1 % 7 == 4:
    print("It's Thursday.");
if num1 % 7 == 5:
    print("It's Friday.");
if num1 % 7 == 6:
    print("It's Saturday.");
if num1 % 7 == 0:
    print("It's Sunday.");
'''
'''
num = int(input("Enter number : "));
if num == 1:
    print("It's 1.");
else:
    print("It's not 1.");
'''
'''
arr = [1,2,3,4,5]; # 학습하지 않은 내용 : 리스트 C언어의 배열과 같음
na = int(input("Enter numbers to find : "));
if na in arr:
    print("arr : ",arr,na,"you are looking for exist");
else:
    print("arr : ",arr,na,"you are looking for does not exist");
print("Result :",na in arr);
'''
'''
st = "Hello Python Fun";
na = input("Enter the string you want to find : ");
if na in st:
    print("st :",st,"\tSearch string :",na,"exist");
else:
    print(na,"does not exist in st :",st);
'''
'''
old_id = input("Enter ID to save : ");
print("It's a certification program");
print("Login");
new_id = input("Enter ID : ");
if old_id == new_id:
    print("I passed the certification");
else:
    print("certification failed");
'''
'''
num = int(input("Enter num : "));
if num % 3 == 0:
    if num % 2 == 0:
        print("num is a multiple of 3 and an even number");
print("I am the next sentence.");
'''
'''
num = int(input("Enter num : "));
if num > 0:
    if num % 2 == 0:
        print("num is a positive even number");
    else:
        print("num is a positive odd number");
else:
    print("num is a negative number");
print("I am the next sentence.");
'''
'''
num = int(input("Enter num : "));
if num > 0:
    print("num is a positive number");
elif num < 0:
    print("num is a negative number");
else:
    print("num is 0");
'''
'''
#Example Problem
#Enter name, student number, score(Korean, English, Math) => print name, student number, average, grade
#grade (average>=90 A, average>=80 B, average>=70 C, average>=60 D, average<60 F)
name = input("Enter name : ")
num = input("Enter student number : ")
kor = int(input("Enter Korean score: "))
eng = int(input("Enter English score: "))
math = int(input("Enter Math score: "))
sum = kor+eng+math
avg = round(sum/3,2)
print("=========== Result ===========")
print("Name :",name)
print("student number :",num)
print("average :",avg)
if avg >= 90:
    print("grade : A")
elif avg >= 80:
    print("grade : B")
elif avg >= 70:
    print("grade : C")
elif avg >= 60:
    print("grade : D")
else:
    print("grade : F")
'''
'''
#Example Problem
# coffee : 2000won (If you drink more than 10 cups, you'll get 1,500 won for the excess.)
cnt=int(input("a few cups of coffee? "))
if cnt <= 10:
    price=cnt*2000
    print("total price is",price,"won.")
else:
    price1 = 10*2000
    price2 = (cnt-10)*1500
    print("total price is",price1+price2,"won.")
'''
'''
#Example Problem
num = int(input('Enter integer : '))
if num==0: 
	print(num,"is not a multiple of 3 or a multiple of 4.");
elif num%3==0 and num%4==0: 
	print(num,"is a multiple of 3 and a multiple of 4.");
elif num%3==0:
	print(num,"is a multiple of 3.");
elif num%4==0:
	print(num,"is a multiple of 4.");
else: 
	print(num,"is not a multiple of 3 or a multiple of 4.");
'''
'''
#Example Problem
#The basic fare is 30000 won only for a 30-minute flight, and an additional 5000 won will be added every 10 minutes.
#Flight Fare Calculator
money=30000;
time = int(input("Time(minutes) on the plane: "))
time-=30
if time > 9:
    money=money+time//10*5000
print(money,"won.")
'''