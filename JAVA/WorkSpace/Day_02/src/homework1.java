import java.util.Scanner;

public class homework1 
{
	public static void main(String[] args) 
	{
		int num1 , num2;
		Scanner input = new Scanner(System.in);
		int result;
		
		System.out.print("Enter first integer: ");
		num1 = input.nextInt();
		System.out.print("Enter second integer: ");
		num2 = input.nextInt();
		
		result = num1 > num2 ? num1 : num2;
		
		System.out.println("The larger number is " + result);
	}
}
