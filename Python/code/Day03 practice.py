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