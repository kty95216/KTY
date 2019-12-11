import java.util.Scanner;

public class Add2
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		
		int x;
		int y;
		int sum;
		
		System.out.println("첫번째 값을 입력하시오 : ");
		x = input.nextInt();
		System.out.println("두번째 값을 입력하시오 : ");
		y = input.nextInt();
		
		sum = x + y;
		
		System.out.println("x + y = " + sum + "입니다.");
	}
}
