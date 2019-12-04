/*
//예시 코딩 문제 : 정수 2개 입력 , 입력받은 정수 2개를 서로 더해서 출력
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

	printf("두 수의 합 : %d + %d = %d", x, y, result);

	return 0;
}
*/

/*
//예시 코딩 문제 : 영문 대문자를 입력받아 영문 소문자로 출력
#include <stdio.h>

int main()
{
	char A;
	char a;

	printf("대문자 입력 : ");
	scanf("%c", &A);
	a = A + 32;

	printf("%c의 소문자는 %c이다.\n", A, a);
	return 0;
}
*/

//예시 코딩 문제 : 학생의 국어점수 , 영어점수 , 수학점수을 입력한 뒤 합계와 평균을 구하시오.

/*
#include <stdio.h>

int main()
{
	int kor,eng,math,sum;
	float avg;
	int class = 3;

	printf("====================\n");
	printf("  이 름 : 홍 길 동\n");
	printf("====================\n");
	printf(" 국 어 : ");
	scanf("%d", &kor);
	printf(" 영 어 : ");
	scanf("%d", &eng);
	printf(" 수 학 : ");
	scanf("%d", &math);
	printf("====================\n");
	sum = kor + eng + math;
	avg = (float)sum / class;
	printf(" 합 계 : %d\n", sum);
	printf(" 평 균 : %.2f\n", avg);
	printf("====================\n");

	return 0;
}
*/

/*
//예시 코딩 문제 : x가 양수인지 ? 음수인지 ? 0인지 ? 확인하는 프로그램 만드시오.
#include <stdio.h>

int main()
{
	int x;

	printf("x를 입력 하세요 : ");
	scanf("%d",&x);

	if (x > 0)
	{
		printf("x는 양수입니다.");
	}
	else if (x == 0)
	{
		printf("x는 0입니다.");
	}
	else
	{
		printf("x는 음수입니다.");
	}

	return 0;
}
*/

/*
//예시 코딩 문제 : 입력 받은 문자가 대문자이면 소문자출력 , 소문자이면 대문자출력 , 영문자가 아니면 ->영문자를 입력해주세요. 출력
//and연산 명령어 질문 부호 한번에 2개 불가능 질문 조건부연산자도 참,거짓으로 판별?
#include <stdio.h>

int main()
{
	char A;

	printf("영문자를 입력 : ");
	scanf("%c",&A);

	if (65 <= A && A <= 90)
	{
		printf("%c의 소문자 : %c", A, A + 32);
	}
	else if (97 <= A && A <= 122)
	{
		printf("%c의 대문자 : %c", A, A - 32);
	}
	else
	{
		printf("영문자가 아니니 영문자를 다시 입력해주세요");
	}

	return 0;
}
*/

/*
// 예시 코딩 문제 : 1~9사이의 숫자 입력 , 해당 숫자의 구구단 출력
#include <stdio.h>

int main()
{
	int i;
	int a;

	i = 1;

	printf("1~9사이의 숫자를 입력하세요 : ");
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
//예시 코딩 문제 : 1~9사이의 숫자 입력 , 해당 숫자의 구구단 출력 , 1~9사이의 숫자가 아니면 다시입력할수 있도록
#include <stdio.h>

int main()
{
	int i;
	int a;

	i = 1;
	do
	{
		printf("1~9사이의 숫자 : ");
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
//♨ 예시 코딩 문제 : *****\n*****\n*****\n*****\n***** 출력
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
//♨ 예시 코딩 문제 : *\n**\n***\n****\n***** 출력
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
//예시 코딩 문제 : 정수 입력 , 입력받은 정수를 모두 더해주는 프로그램(0을 입력받는 즉시 프로그램 종료)
#include <stdio.h>

int main()
{
	int n;
	int sum = 0;

	while (1)
	{
		printf("정수 입력 (0:종료) : ");
		scanf("%d", &n);
		if (n == 0)
		{
			break;
		}
		sum += n;
	}
	printf("총 합 : %d\n", sum);
	return 0;
}
*/

/*
//예시 코딩 문제 : +,-,*,/ 연산자를 사용하여 코드를 작성 , 연산자에 q를 입력 받기 전까지 프로그램을 종료하지 않는다. 계산기 프로그램
#include <stdio.h>

int main()
{
	int a, b;
	char c;

	while (1)
	{
		printf("=== 계산기 프로그램 ===\n");
		printf("연산자 입력 (+,-,*,/) : ");
		scanf(" %c", &c);
		if (c == 113)
		{
			printf("프로그램을 종료합니다.");
			break;
		}
		printf("첫 번째 숫자 입력 : ");
		scanf("%d", &a);
		printf("두 번째 숫자 입력 : ");
		scanf("%d", &b);
		switch (c)
		{
		case 43:
			printf("====== 결 과 ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a + b);
			break;
		case 45:
			printf("====== 결 과 ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a - b);
			break;
		case 42:
			printf("====== 결 과 ======\n");
			printf("%d %c %d = %d\n\n", a, c, b, a * b);
			break;
		case 47:
			printf("====== 결 과 ======\n");
			printf("%d %c %d = %.2f\n\n", a, c, b, (float)a / b);
			break;
		}
	}
	return 0;
}
*/

/*
//예시 코딩 문제 : 동전 앞 뒤 맞추기 , 1 or 2의 랜덤 수를 추출 한 뒤 사용자가 입력한 값과 비교
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
	printf("동전 앞 뒤 맞추기\n");
	printf("입력 하세요 (0.앞면, 1.뒷면) : ");
	scanf("%d", &coin);
	if (n == coin)
	{
		printf("맞췄습니다.^^");
	}
	else
	{
		printf("틀렸습니다.ㅠㅠ");
	}
	return 0;
}
*/

/*
//예시 코딩 문제 : 컴퓨터와 가위 바위 보 게임 프로그램 제작
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

		printf("=== 가위 바위 보 게임 ===\n");
		printf("숫자를 선택하세요(1.가위/2.바위/3.보/4,프로그램 종료) : ");
		scanf("%d", &my);
		if (my == 4)
		{
			printf("프로그램을 종료합니다\n");
			break;
		}
		printf("======== 결과 ===========\n");
		if (my == 1)
		{
			printf("당신은 가위를 냈습니다.\n");
		}
		else if (my == 2)
		{
			printf("당신은 바위를 냈습니다.\n");
		}
		else if (my == 3)
		{
			printf("당신은 보를 냈습니다.\n");
		}
		if (com == 1)
		{
			printf("컴퓨터는 가위를 냈습니다.\n");
		}
		else if (com == 2)
		{
			printf("컴퓨터는 바위를 냈습니다.\n");
		}
		else if (com == 3)
		{
			printf("컴퓨터는 보를 냈습니다.\n");
		}
		printf("========================\n");
		if (com == my)
		{
			printf("비겼습니다.\n\n");
		}
		else if (((com == 1) && (my == 2)) || ((com == 2) && (my == 3)) || ((com == 3) && (my == 1)))
		{
			printf("유저가 이겼습니다.^^\n\n");
		}
		else if (((com == 1) && (my == 3)) || ((com == 2) && (my == 1)) || ((com == 3) && (my == 2)))
		{
			printf("컴퓨터가 이겼습니다.ㅠ.ㅠ\n\n");
		}
	}
	return 0;
}
*/

/*
//예시 코딩 문제 : UP & Down Game (컴퓨터는 1~99의 랜덤한 숫자를 맞추는 게임) , Game Score는 최단기록 출력
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
					printf("<<  정  답  >>\n\n");
					if (score == 0 || score > count)
					{
						printf("신기록!!!\n\n");
						score = count;
					}
					break;
				}
			}
			break;
		case 2:
			printf("당신의 최단 기록은 %d번 입니다.\n\n", score);
			break;
		case 3:
			printf("프로그램을 종료합니다.\n");
			return 0;
			break;
		}
	}
	return 0;
}
*/

/*
//예시 코딩 문제 : Baskin Robbins 31 Game 제작 , 1 ~ 31 순차적으로 2사람이 외침 , 31외치면 패배 , 한명당 최대 3번까지 숫자를 외칠수 있음 , 컴퓨터 인공지능 높이기
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
						printf("\n나의 패배\n\n");
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
						printf("\n나의 승리\n\n");
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
// 예시 코딩 문제 : 정수 2개 입력 받아 , 더해서 반환해 주는 함수 , 나눈후 실수로 반환
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
//예시 코딩 문제 : 대소문자 섞인 문자열을 전부 소문자로 전부 대문자로 각각 변환
#include <stdio.h>

int main()
{
	char string[10] = "Apple";
	int i;

	printf("string = %s\n", string);
	printf("소문자로 변환\n");
	for (i = 0; i < sizeof(string); i++)
	{
		if ('A' <= string[i] && string[i] <= 'Z')
		{
			string[i] = string[i] + 32;
		}
	}
	printf("string = %s\n", string);
	printf("대문자로 변환\n");
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
//예시 코딩 문제
#include <stdio.h>

int main()
{
	char string[] = "Reverse";	//선언과 동시에 값을 입력해주면 변수의갯수 생략가능
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
//버블정렬을 사용하여 오름차순으로 정렬
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