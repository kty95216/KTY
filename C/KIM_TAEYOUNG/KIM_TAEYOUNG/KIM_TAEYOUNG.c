/*
//���� �ڵ� ���� : ���� 2�� �Է� , �Է¹��� ���� 2���� ���� ���ؼ� ���
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

	printf("�� ���� �� : %d + %d = %d", x, y, result);

	return 0;
}
*/


/*
//���� �ڵ� ���� : ���� �빮�ڸ� �Է¹޾� ���� �ҹ��ڷ� ���
#include <stdio.h>

int main()
{
	char A;
	char a;

	printf("�빮�� �Է� : ");
	scanf("%c", &A);
	a = A + 32;

	printf("%c�� �ҹ��ڴ� %c�̴�.\n", A, a);
	return 0;
}
*/

//���� �ڵ� ���� : �л��� �������� , �������� , ���������� �Է��� �� �հ�� ����� ���Ͻÿ�.

/*
#include <stdio.h>

int main()
{
	int kor,eng,math,sum;
	float avg;
	int class = 3;

	printf("====================\n");
	printf("  �� �� : ȫ �� ��\n");
	printf("====================\n");
	printf(" �� �� : ");
	scanf("%d", &kor);
	printf(" �� �� : ");
	scanf("%d", &eng);
	printf(" �� �� : ");
	scanf("%d", &math);
	printf("====================\n");
	sum = kor + eng + math;
	avg = (float)sum / class;
	printf(" �� �� : %d\n", sum);
	printf(" �� �� : %.2f\n", avg);
	printf("====================\n");

	return 0;
}
*/

/*
//���� �ڵ� ���� : x�� ������� ? �������� ? 0���� ? Ȯ���ϴ� ���α׷� ����ÿ�.
#include <stdio.h>

int main()
{
	int x;

	printf("x�� �Է� �ϼ��� : ");
	scanf("%d",&x);

	if (x > 0)
	{
		printf("x�� ����Դϴ�.");
	}
	else if (x == 0)
	{
		printf("x�� 0�Դϴ�.");
	}
	else
	{
		printf("x�� �����Դϴ�.");
	}

	return 0;
}
*/

/*
//���� �ڵ� ���� : �Է� ���� ���ڰ� �빮���̸� �ҹ������ , �ҹ����̸� �빮����� , �����ڰ� �ƴϸ� ->�����ڸ� �Է����ּ���. ���
//and���� ��ɾ� ���� ��ȣ �ѹ��� 2�� �Ұ��� ���� ���Ǻο����ڵ� ��,�������� �Ǻ�?
#include <stdio.h>

int main()
{
	char A;

	printf("�����ڸ� �Է� : ");
	scanf("%c",&A);

	if (65 <= A && A <= 90)
	{
		printf("%c�� �ҹ��� : %c", A, A + 32);
	}
	else if (97 <= A && A <= 122)
	{
		printf("%c�� �빮�� : %c", A, A - 32);
	}
	else
	{
		printf("�����ڰ� �ƴϴ� �����ڸ� �ٽ� �Է����ּ���");
	}

	return 0;
}
*/

/*
// ���� �ڵ� ���� : 1~9������ ���� �Է� , �ش� ������ ������ ���
#include <stdio.h>

int main()
{
	int i;
	int a;

	i = 1;

	printf("1~9������ ���ڸ� �Է��ϼ��� : ");
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
//���� �ڵ� ���� : 1~9������ ���� �Է� , �ش� ������ ������ ��� , 1~9������ ���ڰ� �ƴϸ� �ٽ��Է��Ҽ� �ֵ���
#include <stdio.h>

int main()
{
	int i;
	int a;

	i = 1;
	do
	{
		printf("1~9������ ���� : ");
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
//�� ���� �ڵ� ���� : *****\n*****\n*****\n*****\n***** ���
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
//�� ���� �ڵ� ���� : *\n**\n***\n****\n***** ���
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
//���� �ڵ� ���� : ���� �Է� , �Է¹��� ������ ��� �����ִ� ���α׷�(0�� �Է¹޴� ��� ���α׷� ����)
#include <stdio.h>

int main()
{
	int n;
	int sum = 0;

	while (1)
	{
		printf("���� �Է� (0:����) : ");
		scanf("%d", &n);
		if (n == 0)
		{
			break;
		}
		sum += n;
	}
	printf("�� �� : %d\n", sum);
	return 0;
}
*/

/*
//���� �ڵ� ���� : +,-,*,/ �����ڸ� ����Ͽ� �ڵ带 �ۼ� , �����ڿ� q�� �Է� �ޱ� ������ ���α׷��� �������� �ʴ´�. ���� ���α׷�
#include <stdio.h>

int main()
{
	int a, b;
	char c;

	while (1)
	{
		printf("=== ���� ���α׷� ===\n");
		printf("������ �Է� (+,-,*,/) : ");
		scanf(" %c", &c);
		if (c == 113)
		{
			printf("���α׷��� �����մϴ�.");
			break;
		}
		printf("ù ��° ���� �Է� : ");
		scanf("%d", &a);
		printf("�� ��° ���� �Է� : ");
		scanf("%d", &b);
		switch (c)
		{
		case 43:
			printf("====== �� �� ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a + b);
			break;
		case 45:
			printf("====== �� �� ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a - b);
			break;
		case 42:
			printf("====== �� �� ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a * b);
			break;
		case 47:
			printf("====== �� �� ======\n");
			printf("%d %c %d = %.2f\n\n", a, c, b, (float)a / b);
			break;
		}
	}
	return 0;
}
*/

/*
//���� �ڵ� ���� : ���� �� �� ���߱� , 1 or 2�� ���� ���� ���� �� �� ����ڰ� �Է��� ���� ��
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
	printf("���� �� �� ���߱�\n");
	printf("�Է� �ϼ��� (0.�ո�, 1.�޸�) : ");
	scanf("%d", &coin);
	if (n == coin)
	{
		printf("������ϴ�.^^");
	}
	else
	{
		printf("Ʋ�Ƚ��ϴ�.�Ф�");
	}
	return 0;
}
*/

/*
//���� �ڵ� ���� : ��ǻ�Ϳ� ���� ���� �� ���� ���α׷� ����
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

		printf("=== ���� ���� �� ���� ===\n");
		printf("���ڸ� �����ϼ���(1.����/2.����/3.��/4,���α׷� ����) : ");
		scanf("%d", &my);
		if (my == 4)
		{
			printf("���α׷��� �����մϴ�\n");
			break;
		}
		printf("======== ��� ===========\n");
		if (my == 1)
		{
			printf("����� ������ �½��ϴ�.\n");
		}
		else if (my == 2)
		{
			printf("����� ������ �½��ϴ�.\n");
		}
		else if (my == 3)
		{
			printf("����� ���� �½��ϴ�.\n");
		}		
		if (com == 1)
		{
			printf("��ǻ�ʹ� ������ �½��ϴ�.\n");
		}
		else if (com == 2)
		{
			printf("��ǻ�ʹ� ������ �½��ϴ�.\n");
		}
		else if (com == 3)
		{
			printf("��ǻ�ʹ� ���� �½��ϴ�.\n");
		}
		printf("========================\n");
		if (com == my)
		{
			printf("�����ϴ�.\n\n");
		}
		else if (((com == 1) && (my == 2)) || ((com == 2) && (my == 3)) || ((com == 3) && (my == 1)))
		{
			printf("������ �̰���ϴ�.^^\n\n");
		}
		else if (((com == 1) && (my == 3)) || ((com == 2) && (my == 1)) || ((com == 3) && (my == 2)))
		{
			printf("��ǻ�Ͱ� �̰���ϴ�.��.��\n\n");
		}
	}	
	return 0;
}
*/

/*
//���� �ڵ� ���� : UP & Down Game (��ǻ�ʹ� 1~99�� ������ ���ڸ� ���ߴ� ����) , Game Score�� �ִܱ�� ���
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
				printf("\ninput number : ");
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
					printf("<<  ��  ��  >>\n\n");
					if (score == 0 || score > count)
					{
						printf("�ű��!!!\n\n");
						score = count;
					}
					break;
				}
			}
			break;
		case 2:
			printf("����� �ִ� ����� %d�� �Դϴ�.\n\n", score);
			break;
		case 3:
			printf("���α׷��� �����մϴ�.\n");
			return 0;
			break;
		}
	}
	return 0;
}
*/

/*
//���� �ڵ� ���� : Baskin Robbins 31 Game ���� , 1 ~ 31 ���������� 2����� ��ħ , 31��ġ�� �й� , �Ѹ�� �ִ� 3������ ���ڸ� ��ĥ�� ���� , ��ǻ�� �ΰ����� ���̱�
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
						printf("\n���� �й�\n\n");
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
						printf("\n���� �¸�\n\n");
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
// ���� �ڵ� ���� : ���� 2�� �Է� �޾� , ���ؼ� ��ȯ�� �ִ� �Լ� , ������ �Ǽ��� ��ȯ
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
//���� �ڵ� ���� : ��ҹ��� ���� ���ڿ��� ���� �ҹ��ڷ� ���� �빮�ڷ� ���� ��ȯ
#include <stdio.h>

int main()
{
	char string[10] = "Apple";
	int i;

	printf("string = %s\n", string);
	printf("�ҹ��ڷ� ��ȯ\n");
	for (i = 0; i < sizeof(string); i++)
	{
		if ('A' <= string[i] && string[i] <= 'Z')
		{
			string[i] = string[i] + 32;
		}
	}
	printf("string = %s\n", string);
	printf("�빮�ڷ� ��ȯ\n");
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
//���� �ڵ� ����
#include <stdio.h>

int main()
{
	char string[] = "Reverse";	//����� ���ÿ� ���� �Է����ָ� �����ǰ��� ��������
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
//���������� ����Ͽ� ������������ ����
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