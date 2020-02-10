'''
print("Hello~~ Python ^^"); print("hello")
print('It's the first day of Python'); print("Python Start")
'''
'''
print("Hello \"weekend\" Python");
print("Hello \nPython");
print("Exciting");print("Python")
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
#Example
print("My name is Kim Tae Young\nI am 24 years old\nMy address is Anyang");
print("My name is Kim Tae Young\n"
"i am 24 years old\n"
"My address is Anyang");
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
print("double quotation mark\"");
print("single quotation mark '");
print('double quotation mark "');
print('single quotation mark \'');
'''
'''
print('expression \ way');
print('expression \2 way');
print('expression \\2 way');
#print('way of expression\') #error code
print('way of expression\\');
'''
'''
print("123 + 123");
print(542 - 242);
print(2 * 123);
print(120 / 3);
'''
'''
print("Addition result : ",123 + 123);
print("Subtraction result : ",542 - 242);
print("Multiplication result :",2 * 123)
print("Division result : ",123 / 3);
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
print("Binary number :",bin(0b01111011));
print("octal number :",oct(0b01111011));
print("hexadecimal number :",hex(0b01111011));
print("decimal number :",0b01111011);
'''
'''
print("%d"%123);
#print("%d %d" % 123); #error code
#print("%d" % (123 , 321)); #error code
print("%d %d"%(123 , 321));
print("%d + %d = %d"%(123 , 321 , 123 + 321));
'''
'''
print("decimal integer : %d"%123);
print("decimal integer : %d"%0o173);
print("decimal integer : %d"%0x7b);

print("octal integer : %o"%123);
print("octal integer : %o"%0o173);
print("octal integer : %o"%0x7b);

print("hexadecimal integer : %x"%123);
print("hexadecimal integer : %x"%0o173);
print("hexadecimal integer : %x"%0x7b);
'''
'''
print("expression of integer  : %d"%123);
print("expression of integer  : %d"%123.623);
print("expression of integer  : %d %d"%(123,456));

print("\nexpression of real number : %f"%456);
print("expression of real number : %.2f"%456.456);
print("expression of real number : %f %f"%(456.456 , 123.123));
'''
'''
print("expression of character : %c %c"%("K","R"));
print("expression of character : %c %c"%('E','S'));

print("\nexpression of string : %s"%"Hello");
print("expression of string : %s\t%s"%('String',"way of expression"));
'''
'''
print("Default value : %d"%123);
print("Setting value : %5d"%123);
print("Setting value : %05d"%123);
print("Setting value : %5d%5d"%(123,123));
print("Setting value : %-5d%-5d"%(123,123));
'''
'''
print("Default value : %f"%123.45678);
print("Setting value : %10.3f"%123.45678);
print("Setting value : %2.1f"%123.45678);
print("Setting value : %.2f"%123.45678);
'''
'''
print("Default value : %s"%"python test");
print("Setting value : %20s"%"python test");
'''
'''
print('%s is %d years old'%('KIM',38));
print('{} is {} years old'.format('LEE',35));
'''
'''
print("%10s , %-10s"%('Right','Left'));
print("{:>10} , {:<10}".format('Right','Left'));
print('{:^10}'.format('Center'));
'''
'''
print('{:,}'.format(1000000));
'''