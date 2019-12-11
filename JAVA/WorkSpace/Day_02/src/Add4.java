import java.util.Scanner;

public class Add4 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		
		double n1 = 0;
		double n2 = 0;
		double result = 0;
		
		System.out.print("n1 숫자 입력 : ");
		n1 = input.nextDouble();
		System.out.print("n2 숫자 입력 : ");
		n2 = input.nextDouble();
		
		result = n1 > n2 ? n1 : n2;
		
		System.out.println("더 큰 숫자는 : " + result);
	}
}