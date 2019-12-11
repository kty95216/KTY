import java.util.Scanner;

public class homework1 
{
	public static void main(String[] args) 
	{
		int num1 , num2;
		Scanner input = new Scanner(System.in);
		int result;
		
		System.out.print("첫번째 정수 입력하세요 : ");
		num1 = input.nextInt();
		System.out.print("두번째 정수 입력하세요 : ");
		num2 = input.nextInt();
		
		result = num1 > num2 ? num1 : num2;
		
		System.out.println("더 큰 숫자는 : " + result + "이다.");
	}
}
