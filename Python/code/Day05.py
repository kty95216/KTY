'''
i = 0;
while i < 5:
    print(i,"dependent sentence");
    i += 1;

print("next sentence");
'''
'''
i = 1;
odd, even = 0,0;
while i <= 10:
    if i % 2 == 0:
        even += i;
    else:
        odd += i;
    i += 1;
print("Sum of 1-10 even :",even);
print("Sum of 1-10 odd :",odd);
'''
'''
#while command -> for command
i , odd , even =0,0,0;
for i in range(1, 11, 1):
    if i % 2 == 0:
        even += i;
    else:
        odd += i;
print("Sum of 1-10 even :",even);
print("Sum of 1-10 odd :",odd);
'''
'''
i = 0;
while i < 5:
    print(i, "dependent sentence");
    i += 1;
else:
    print("If the conditional expression is false :",i);
print("next sentence");
'''
'''
i = 1;
while True:
    print(i,"dependent sentence",end=" ");
    i += 1 ;
'''
'''
i = 1;
flag = True
while flag:
    print(i,"dependent sentence",end=" ");
    if i == 10:
        flag = True-1;
    i += 1;
'''
'''
i = 0;
while True:
    if i == 3:
        break
        print("3----print");
    print(i,"print");
    i += 1;
print("next sentence");
'''
'''
i = 0;
while i < 5:
    i += 1;
    if i == 3:
        continue
        print("3----print");
    print(i,"print");
print("next sentence");
'''
'''
num, result, i = 0, 0, 1;
while True:
    num = int(input("Enter number between 1 and 10 : "));
    if num < 1 or num > 10:
        print("Incorrect input again");
        continue;
    break
else:
    print("next...");
while i <= num :
    result += i;
    i += 1;
else:
    print("sum from 1 to",num,":",result);
'''
'''
#Example problem
num, result, i = 0, 0, 1;
aaa = True;
while aaa:
    num = int(input("Enter number between 1 and 10 : "));
    if num < 1 or num > 10:
        print("Incorrect input again");
        continue;
    aaa = False;
else:
    print("next...");
while i <= num :
    result += i;
    i += 1;
else:
    print("sum from 1 to",num,":",result);
'''
'''
#Enter 10 to 20 number and output from 1 to the number of input
num, result, i = 0, 0, 1
while True :
    num = int(input("Enter number between 10 and 20 : "))
    if num < 10 or num > 20 :
        print("Incorrect input again")
        continue
    break
while i <= num :
    result += i
    i += 1
else:
    print("the sum of 1 to",num,":",result)
'''
'''
#Example problem
#Change the for command below to while command
#for i in range(0, 3, 1):
#    for k in range(0, 5, 1):
#        if k == 3:
#            break
#        print("(i : %d\tk : %d)"%(i ,k))
i,k=0,0
while i < 3:
    k=0
    while k < 5:
        if k == 3:
            break
        print("(i : %d\tk : %d)"%(i, k))
        k+=1
    i+=1
'''
'''
#Example problem
#There are a pair of female and male rats in a warehouse where 100 kilograms of rice is stored.
#A mouse eats 20 grams of rice a day, and every 10 days (10, 20, 30) the number of mice doubles.
#Will all the rice in the warehouse be eaten by mice in a matter of days? And how many mice are there in total?
#(Condition of doubling after eating rice)
rice = 100000; mouse = 2; day=1;
while rice>0:
    rice -= mouse*20
    if day%10 == 0:
        mouse *= 2
    if rice <= 0:
        break
    day+=1
print(day,'days',mouse,'mice')
'''
'''
#Example problem
#Vending machine
money, j = 0, 0;
money = int(input('Enter the charge : '))
while True:
    print("==========coffee, cocoa vending machine==========")
    print("1. ceffee(200)\t2. cocoa(250)\t3. Return\t4. exit")
    print("Remaining money :",money)
    j = int(input("Please select a menu >>> "))
    if j == 4:
        break
    elif ((j == 1 and money < 200) or (j == 2 and money < 250)):
        print("There is not enough charge\n")
    elif j == 1:
        print("Enjoy your drink.\n")
        money -= 200
    elif j == 2:
        print("Enjoy your drink.\n")
        money -= 250
    elif j == 3:
        print("Return charge :",money,"\n")
        money = 0
    else:
        print("You've entered something wrong.\n")
print("Program exit")
'''