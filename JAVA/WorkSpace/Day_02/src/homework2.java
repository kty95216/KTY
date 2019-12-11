import java.util.Scanner;

public class homework2 
{
	public static void main(String[] args) 
	{
		//2번, 3개 정수 입력받아서, 가장큰 수
		
		Scanner input = new Scanner(System.in);//입력받을 스캐너
		int num1, num2, num3; //3개의 정수 저장할 변수
		int result; //결과값
		
		System.out.print("첫번째 정수 입력하세요 : ");
		num1 = input.nextInt();
		System.out.print("두번째 정수 입력하세요 : ");
		num2 = input.nextInt();
		System.out.print("세번째 정수 입력하세요 : ");
		num3 = input.nextInt();
		
		//num1과 num2중 큰 수를 result에 저장
		result = num1 > num2 ? num1 : num2;
		
		//result와 num3중 큰 수를 result에 저장
		result = result > num3 ? result : num3;
		
		System.out.println(result);
	}
}
