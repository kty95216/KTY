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
#tp1[0] = 100 #Error Code(내부 데이터 변경 불가능하기 때문에 오류)
'''
'''
tpType = "String",100,1.111;
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
print("Sum of tuples : %d"%tt2);
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
pack = 1,2,"packing";
print("packing\npack:",pack);
a,b,c = pack;
print("unpacking\na:",a,"b:",b,"c:",c);
print("packing\npack:",pack);
a=10;
pack = a,b,c;
print("packing\npack:",pack);
'''
'''
tp = 100,200,"function",100,"count";
print("200 positions in tp : ",tp.index(200),"index");
print("100 count in tp : ",tp.count(100),"count");
'''
'''
#Example problem
#Pack several values and print out the stored values.
#(It is not known how many values are stored)(Save 5 values)
#Store the value of the tuple in a list
tp = 10,20,"test",3.3333,40;
ls = [];
for i in range(len(tp)):
    ls.append(tp[i]);
print("tp :",tp);
print("ls :",ls);
print(type(ls));
'''
''''
student = {"Student number":1234 , "name":"Kim Tae Young" , "Department":"IT Department"};
print(student);
mobile = {"Product Name":"Galaxy" , "price":100 , "size":10};
print(mobile);
print(student["Student number"]);
'''
'''
impo = {};
impo["Python"] = "www.python.org";
impo["Naver"] = "www.naver.com";
impo["Google"] = "www.google.com";
print("Python:",impo["Python"]);
print("Naver:",impo["Naver"]);
print("Google:",impo["Google"]);
print(impo);
'''
'''
impo = {};
name = input("Enter key value:");
val = input("Value input:");
impo[name] = val;
print(name,":",impo[name]);
'''
'''
#Example problem
#Select one target, enter the key value and value, save it, and print it out.
#Enter name(key):Kenji
#Enter value(value):Shuriken
#Enter name(key):McCree
#Enter value(value):Flash bomb
#Enter name(key):Farah
#Enter value(value):Rocket Launcher
#Enter name(key):Reaper
#Enter value(value):Shotgun
#Enter name(key):Soldier
#Enter value(value):spiral rocket
#{“Soldier”:“spiral rocket” , “McCree”:“Flash bomb” , “Reaper”:“Shotgun” , “Farah”:“Rocket Launcher” , “Kenji”:“Shuriken”}
overwatch = {};
for i in range(0,5,1):
    name = input("Enter name(key):");
    val = input("Enter value(value):");
    overwatch[name] = val;
print(overwatch);
'''
'''
num = {1:"One" , 2:"Two" , 3:"Three" , 4:"Four"};
print("keys()키:",num.keys());
print();
print("values()값:",num.values());
'''
'''
num = {1:"One" , 2:"Two" , 3:"Three" , 4:"Four"};
print("num.keys():",num.keys());
print("list(num):",list(num));
print("list(num.keys()):",list(num.keys()));
print();
print("num.values():",num.values());
print("list(num.values()):",list(num.values()));
'''
'''
singer = {};
singer["Singer name"]=input("Enter Singer name:");
singer["Member"]=input("Enter number of members:");
singer["Representative song"]=input("Enter representative song:");
for i in singer.keys():
    print("%s:%s"%(i,singer[i]));
print(singer);
'''
'''
menu = {}; bl = True; num = 0;
while bl:
    print("1.Menu registration");
    print("2.View prices by menu");
    print("3.Price modification");
    print("4.Exit");
    num = int(input(">>>"));
    if num == 1:
        name = input("Enter menu:");
        menu[name] = input("Enter price:");
    elif num == 2:
        for i in menu.keys():
            print(i,":",menu[i]);
    elif num == 3:
        name = input("Enter a list to modify:");
        menu[name] = input("Modified price:");
    elif num == 4:
        print("Program exit");
        bl = False;
'''
'''
num = {1:"One" , 2:"Two" , 3:"Three" , 4:"Four" , 5:"Five"};
print(num);
print("num.get(3):",num.get(3));    # Same as # code below
#print("num.get(3):",num[3]);
print("num.get(9):",num.get(9));
#print("num.get(9):",num[9]);
'''
'''
student = {"Student number":1234 , "Name":"Kim Tae Young" , "Department":"IT Department"};
print(student["Student number"]);
print(student["Name"]);
print(student["Department"]);
print();
print(student.items());
print();
print(student);
'''
'''
name = {"Kim":"Tae Young" , "City":"Seoul" , "Python":"Program"};
for key,value in name.items():
    print(key,":",value);
print("Delete:",name.clear());
print("Value after deletion:",name);
'''
'''
num = {1:"One" , 2:"Two" , 3:"Three" , 4:"Four" , 5:"Five"};
print("Value before change:",num);
print();
print("num.setdefault(9):",num.setdefault(9,"Nine~~~~~"));
print();
print("Value after change:",num);
print();
print("Value of num.get(9):",num.get(9));
'''
'''
dic = {};
ls = [];
ls.append(input("Enter key value to register:"));
ls.append(input("Enter key value to register:"));
ls.append(input("Enter key value to register:"));
dic = dic.fromkeys(ls);
print("dic key setting:",dic);
dic=dic.fromkeys(ls,0);
print("dic key & value setting:",dic);
'''