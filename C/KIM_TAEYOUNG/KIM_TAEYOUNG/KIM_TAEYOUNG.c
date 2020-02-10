/*
//Example problem : Outputs by entering 2 integers and adding 2 entered integers
#include <stdio.h>

int main()
{
	int x;
	int y;
	int result;

	printf("x : ");
	scanf("%d", &x);
	printf("y : ");
	scanf("%d", &y);

	result = x + y;

	printf("Sum of two numbers : %d + %d = %d", x, y, result);

	return 0;
}
*/

/*
//Example problem : Enter uppercase letters to print lowercase letters in English
#include <stdio.h>

int main()
{
	char A;
	char a;

	printf("Enter uppercase letters : ");
	scanf("%c", &A);
	a = A + 32;

	printf("The lower case letter of %c is %c.\n", A, a);
	return 0;
}
*/

//Example problem : Enter the student's Korean, English, and Math scores and get the sum and average.
/*
#include <stdio.h>

int main()
{
	int kor,eng,math,sum;
	float avg;
	int class = 3;

	printf("====================\n");
	printf("NAME : Kim Tae Young  \n");
	printf("====================\n");
	printf("Korean : ");
	scanf("%d", &kor);
	printf("English : ");
	scanf("%d", &eng);
	printf("Math : ");
	scanf("%d", &math);
	printf("====================\n");
	sum = kor + eng + math;
	avg = (float)sum / class;
	printf("Sum : %d\n", sum);
	printf("Average : %.2f\n", avg);
	printf("====================\n");

	return 0;
}
*/

/*
//Example problem : Create a program that checks whether x is positive number or negative number or zero.
#include <stdio.h>

int main()
{
	int x;

	printf("Enter x : ");
	scanf("%d",&x);

	if (x > 0)
	{
		printf("x is a positive number.");
	}
	else if (x == 0)
	{
		printf("x is zero");
	}
	else
	{
		printf("x is a negative number");
	}

	return 0;
}
*/

/*
//Example problem : If the character you received is uppercase, print lowercase letters. If the character you received is lowercase, print uppercase letters. If the character you typed is not an alphabetic character, make it possible to enter again.
#include <stdio.h>

int main()
{
	char A;

	printf("Enter alphabetic character : ");
	scanf("%c",&A);

	if (65 <= A && A <= 90)
	{
		printf("the lowercase letter of %c : %c", A, A + 32);
	}
	else if (97 <= A && A <= 122)
	{
		printf("the uppercase letter of %c : %c", A, A - 32);
	}
	else
	{
		printf("It's not an English letter, so please re-enter the English characters.");
	}

	return 0;
}
*/

/*
//Example problem : Please enter a number between 1 and 9 and Print the multiplication table of the number you entered.
#include <stdio.h>

int main()
{
	int i;
	int a;

	i = 1;

	printf("Please enter a number between 1 and 9 : ");
	scanf("%d", &a);

	while (i < 10)
	{
		printf("%d * %d = %d\n", a, i, a*i);
		i++;
	}
	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int i;

	printf("<< do - while >>\n");
	i = 0;

	do
	{
		printf("i = %d\n", i);
		i++;
	}
	while (0);

	printf("<< while >>\n");
	i = 0;

	while (0)
	{
		printf("i = %d\n", i);
		i++;
	}
	return 0;
}
*/

/*
//Example problem : If you enter a number between 1 and 9, the multiplication table of the entered number is output. If it's not between 1 and 9, make sure you enter it again.
#include <stdio.h>

int main()
{
	int i;
	int a;

	i = 1;
	do
	{
		printf("a number between 1 and 9 : ");
		scanf("%d", &a);
	}
	while (!(1<=a&&a<=9));

	while (i < 10)
	{
		printf("%d * %d = %d\n", a, i, a*i);
		i++;
	}
	return 0;
}
*/

/*
//Example problem : *****\n*****\n*****\n*****\n*****Output
#include <stdio.h>

int main()
{
	int i, j;

	for (i = 0; i < 5; i++)
	{
		for (j = 0; j < 5; j++)
		{
			printf("*");
		}
		printf("\n");
	}
}
*/

/*
//Example problem : *\n**\n***\n****\n*****Output
#include <stdio.h>

int main()
{
	int i, j;

	for (i = 0; i < 5; i++)
	{
		for (j = 0; j <= i; j++)
		{
			printf("*");
		}
		printf("\n");
	}
}
*/

/*
#include <stdio.h>

int main()
{
	int i;

	i = 0;

	while (i < 10)
	{
		if (i == 3)
		{
			i++;
			continue;
		}
		printf("i = %d\n", i);
		i++;
	}
	return 0;
}
*/

/*
//Example problem : If you enter an integer, the program adds all the integers you have entered(terminate the program as soon as you receive 0)
#include <stdio.h>

int main()
{
	int n;
	int sum = 0;

	while (1)
	{
		printf("Enter an integer (0:End) : ");
		scanf("%d", &n);
		if (n == 0)
		{
			break;
		}
		sum += n;
	}
	printf("Sum : %d\n", sum);
	return 0;
}
*/

/*
//Example problem : +,-,*,/ use operators to write code and do not exit the program until you receive operator "q". Calculator Program
#include <stdio.h>

int main()
{
	int a, b;
	char c;

	while (1)
	{
		printf("===Calculator Program===\n");
		printf("Enter Operator(+,-,*,/) : ");
		scanf(" %c", &c);
		if (c == 113)
		{
			printf("Exit the program.");
			break;
		}
		printf("Enter the first number : ");
		scanf("%d", &a);
		printf("Enter the second number : ");
		scanf("%d", &b);
		switch (c)
		{
		case 43:
			printf("====== Result ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a + b);
			break;
		case 45:
			printf("====== Result ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a - b);
			break;
		case 42:
			printf("====== Result ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a * b);
			break;
		case 47:
			printf("====== Result ======\n");
			printf("%d %c %d = %.2f\n\n", a, c, b, (float)a / b);
			break;
		}
	}
	return 0;
}
*/

/*
//Example problem : coin front, back matching game
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int n;
	int coin;

	srand(time(NULL));
	rand(); rand(); rand();
	srand(rand());

	n = rand() % 2;
	printf("com = %d\n", n);
	printf("Coin front, back matching game\n");
	printf("Enter(0.front, 1.back) : ");
	scanf("%d", &coin);
	if (n == coin)
	{
		printf("That's right^^");
	}
	else
	{
		printf("Incorrect");
	}
	return 0;
}
*/

/*
//Example problem : Rock Paper Scissor game program production
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int com;
	int my;

	srand(time(NULL));
	rand(); rand(); rand();
	srand(rand());

	while (1) {
		com = rand() % 3 + 1;

		printf("=== Rock Paper Scissor game ===\n");
		printf("Please select a number(1.Scissor/2.Rock/3.Paper/4.program end) : ");
		scanf("%d", &my);
		if (my == 4)
		{
			printf("Exit the program\n");
			break;
		}
		printf("======== Result ===========\n");
		if (my == 1)
		{
			printf("User : Scissor\n");
		}
		else if (my == 2)
		{
			printf("User : Rock\n");
		}
		else if (my == 3)
		{
			printf("User : Paper\n");
		}
		if (com == 1)
		{
			printf("Computer : Scissor\n");
		}
		else if (com == 2)
		{
			printf("Computer : Rock\n");
		}
		else if (com == 3)
		{
			printf("Computer : Paper\n");
		}
		printf("========================\n");
		if (com == my)
		{
			printf("draw\n\n");
		}
		else if (((com == 1) && (my == 2)) || ((com == 2) && (my == 3)) || ((com == 3) && (my == 1)))
		{
			printf("User Win^^\n\n");
		}
		else if (((com == 1) && (my == 3)) || ((com == 2) && (my == 1)) || ((com == 3) && (my == 2)))
		{
			printf("Computer Win\n\n");
		}
	}
	return 0;
}
*/

/*
//Example problem : UP & Down Game (a game of matching random numbers between 1 and 99), Game Score is the shortest recorded output
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int com, ply, menu, score, count;

	srand(time(NULL));
	rand(); rand(); rand(); rand();
	srand(rand());

	score = 0;

	while (1)
	{
		printf("==== UP & DOWN Game ====\n");
		printf("1. Game start\n");
		printf("2. Game score\n");
		printf("3. End game\n");
		printf("=> ");
		scanf("%d", &menu);
		switch (menu)
		{
		case 1:
			com = rand() % 99 + 1;
			count = 0;
			while (1)
			{
				printf("\nEnter a number : ");
				scanf("%d", &ply);
				count++;
				if (com > ply)
				{
					printf("<<  U   P  >>\n");
				}
				else if (com < ply)
				{
					printf("<< D O W N >>\n");
				}
				else
				{
					printf("<<  Right Answer  >>\n\n");
					if (score == 0 || score > count)
					{
						printf("new record!!!\n\n");
						score = count;
					}
					break;
				}
			}
			break;
		case 2:
			printf("Your shortest record is %d.\n\n", score);
			break;
		case 3:
			printf("Exit the program.\n");
			return 0;
			break;
		}
	}
	return 0;
}
*/

/*
//Example problem : Baskin Robbins 31 Game (2 people shout in a sequence of 1 to 31, If you shout 31 defeat, you can shout up to 3 times per person, increase computer AI)
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int com, ply, menu, baskin, i, flag;
	int win = 0, lose = 0;

	srand(time(NULL));
	rand(); rand(); rand(); rand();
	srand(rand());

	while (1)
	{
		printf("==== Baskin Robbins 31 ====\n");
		printf("1. Game start\n");
		printf("2. Game score\n");
		printf("3. End game\n");
		printf("\n>");
		scanf("%d", &menu);
		switch (menu)
		{
		case 1:
			baskin = 0; // 1 ~ 31
			flag = 0;
			while (1)
			{
				printf("\ninput number : ");
				scanf("%d", &ply);
				printf("<< player turn >>\n");
				for (i = 0; i < ply; i++)
				{
					baskin++;
					printf("%d!\n", baskin);
					if (baskin == 31)
					{
						printf("\nMy defeat\n\n");
						flag = 1;
						lose++;
						break;
					}
				}
				if (flag)
				{
					break;
				}
				com = rand() % 3 + 1;
				if (baskin >= 27)
				{
					com = 3;
				}
				printf("<< computer turn >>\n");
				for (i = 0; i < com; i++)
				{
					baskin++;
					printf("%d!\n", baskin);
					if (baskin == 30)
					{
						break;
					}
					if (baskin == 31)
					{
						printf("\nMy victory\n\n");
						flag = 1;
						win++;
						break;
					}
				}
				if (flag)
				{
					break;
				}
			}
			break;
		case 2:
			printf("\nW  I  N : %d\n", win);
			printf("L O S E : %d\n\n", lose);
			break;
		case 3:
			return 0;
			break;

		}
	}

	return 0;
}
*/

/*
//Example problem : (1)add function (2)A function that returns a real number after division
#include <stdio.h>

int f(int A, int B)
{
	return A + B;
}
float f2(int A, int B)
{
	return (float)A / B;
}

int main()
{
	printf("f(10,3) : %d\n", f(10, 3));
	printf("f2(10,3) : %f\n", f2(10, 3));

	return 0;
}
*/

/*
#include <stdio.h>

int func(int data)
{
	if (data)
	{
		printf("%d * ", data);
		return func(data - 1) * data;
	}
	printf("\b\b= ");
	return 1;
}
int main()
{
	int i = 3;
	printf("%d\n", func(i));
	return 0;
}
*/

/*
# include <stdio.h>

int main()
{
	int n[5] = { 1,2,3,4,5 };

	printf("sizeof(n) = %d\n", sizeof(n));
	printf("n[0] = %d\n", n[0]);
	printf("n[1] = %d\n", n[1]);
	printf("n[2] = %d\n", n[2]);
	printf("n[3] = %d\n", n[3]);
	printf("n[4] = %d\n", n[4]);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int n;
	int x;

	printf("x = %d\n", &x);
	printf("n = %d\n", &n);

	return 0;
}
*/


/*
# include <stdio.h>

int main()
{
	int n[5] = { 1,2,3,4,5 };

	printf("sizeof(n) = %d\n", sizeof(n));
	printf("n = %d\n", n);
	printf("n[0] = %d\n", &n[0]);
	printf("n[1] = %d\n", &n[1]);
	printf("n[2] = %d\n", &n[2]);
	printf("n[3] = %d\n", &n[3]);
	printf("n[4] = %d\n", &n[4]);

	return 0;
}
*/

/*
//Example problem : Convert uppercase letters to lowercase and lowercase letters to uppercase in mixed-case strings
#include <stdio.h>

int main()
{
	char string[10] = "Apple";
	int i;

	printf("string = %s\n", string);
	printf("Convert to lowercase\n");
	for (i = 0; i < sizeof(string); i++)
	{
		if ('A' <= string[i] && string[i] <= 'Z')
		{
			string[i] = string[i] + 32;
		}
	}
	printf("string = %s\n", string);
	printf("Convert to uppercase\n");
	for (i = 0; i < sizeof(string); i++)
	{
		if ('a' <= string[i] && string[i] <= 'z')
		{
			string[i] = string[i] - 32;
		}
	}
	printf("string = %s\n", string);
	return 0;
}
*/

/*
//Example problem
#include <stdio.h>

int main()
{
	char string[] = "Reverse";
	char tmp;
	int i, j;

	for (i = 0; i < sizeof(string); i++)
	{
		printf("%s\n", string);
		tmp = string[0];
		for (j = 0; j < sizeof(string) - 2; j++)
		{
			string[j] = string[j + 1];
		}
		string[j] = tmp;
	}
	return 0;
}
*/

/*
//Example problem : Ascending Bubble Sort
#include <stdio.h>

int main()
{
	int sort[] = { 15, 9, 1, 8, 60, 99, 100, 70, 50, 20 };
	int i, j;
	int tmp, cnt = 0;
	for (i = 0; i < sizeof(sort) / sizeof(sort[0]); i++)
	{
		printf("%3d ", sort[i]);
	}
	printf("\n");
	for (j = 0; j < sizeof(sort) / sizeof(sort[0]) - 1; j++)
	{
		for (i = 0; i < sizeof(sort) / sizeof(sort[0]) - 1 - j; i++)
		{
			cnt++;
			if (sort[i] > sort[i + 1])
			{
				tmp = sort[i];
				sort[i] = sort[i + 1];
				sort[i + 1] = tmp;
			}
		}
		for (i = 0; i < sizeof(sort) / sizeof(sort[0]); i++)
		{
			printf("%3d ", sort[i]);
		}
		printf("\n");
	}
	printf("count = %d\n", cnt);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int x = 10;
	int *p;

	p = &x;

	printf("x = %d\n", x);
	printf("p = %d\n", p);
	printf("*p = %d\n", *p);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int x = 0x12345678;
	char *p;

	p = &x;

	printf("%x", *p);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int x = 0x12345678;
	short *p;

	p = &x;

	printf("%x", *p);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int n = 10;
	int *p;

	p = &n;
	printf("&n = %d\n", &n);
	printf("p = %d\n", p);
	printf("*p = %d\n", *p);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int n = 10;
	int *p = &n;
	int **pp = &p;
	int ***ppp = &pp;
	int ****pppp = &pp;
	int y = 50;

	n = &y;

	printf("*p = %d\n", *p);
	printf("pp = %d\n", pp);
	printf("**pp = %d\n", **pp);
	printf("ppp = %d\n", ppp);
	printf("***ppp = %d\n", ***ppp);
	printf("pppp = %d\n", pppp);
	printf("****pppp = %d\n", ****pppp);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int n = 10;
	int *p = &n;

	n++;
	p++;

	printf("n = %d\n", n);

	printf("&n = %d\n", &n);
	printf("p = %d\n", p);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int n = 10;
	char *p = &n;

	n++;
	p++;

	printf("n = %d\n", n);

	printf("&n = %d\n", &n);
	printf("p = %d\n", p);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int n = 10;
	char **p = &n;

	n++;
	p++;

	printf("n = %d\n", n);

	printf("&n = %d\n", &n);
	printf("p = %d\n", p);

	return 0;
}
*/

/*
#include <stdio.h>

int main()
{
	int n[5] = { 1,2,3,4,5 };
	int *p;
	p = n;

	printf("n + 1 = %d\n", n + 1);
	printf("p + 1 = %d\n", p + 1);
	printf("*(n + 1) = %d\n", *(n + 1));
	printf("*(p + 1) = %d\n", *(p + 1));
	printf("n[1] = %d\n", n[1]);
	printf("p[1] = %d\n", p[1]);

	return 0;
}
*/