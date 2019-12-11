import java.util.Scanner;

public class homework3 
{
	public static void main(String[] args) 
	{
		//3번. 3개 정수 입력받아서, 중간 값
		Scanner input = new Scanner(System.in);
		int num1, num2, num3;
		int result;
		int max, min;
		
		System.out.print("첫번째 정수 입력하세요 : ");
		num1 = input.nextInt();
		System.out.print("두번째 정수 입력하세요 : ");
		num2 = input.nextInt();
		System.out.print("세번째 정수 입력하세요 : ");
		num3 = input.nextInt();
		
		//중간값 : 전체의 합 - (최대값 + 최소값)
		
		//최대 값
		max = num1 > num2 ? num1 : num2;
		max = max > num3 ? max : num3;
		//최소 값
		min = num1 < num2 ? num1 : num2;
		min = min < num3 ? min : num3;
		
		result = num1 + num2 + num3 - max - min;
		System.out.println("중간값은 : " + result + "입니다.");
	}
}
