import java.util.Scanner;

public class homework3 
{
	public static void main(String[] args) 
	{
		//Program that finds the median value by inputting 3 integers
		Scanner input = new Scanner(System.in);
		int num1, num2, num3;
		int result;
		int max, min;
		
		System.out.print("Enter first integer: ");
		num1 = input.nextInt();
		System.out.print("Enter second integer: ");
		num2 = input.nextInt();
		System.out.print("Enter third integer: ");
		num3 = input.nextInt();
		
		//중간값 : 전체의 합 - (최대값 + 최소값)
		
		//최대 값
		max = num1 > num2 ? num1 : num2;
		max = max > num3 ? max : num3;
		//최소 값
		min = num1 < num2 ? num1 : num2;
		min = min < num3 ? min : num3;
		
		result = num1 + num2 + num3 - max - min;
		System.out.println("The median value is " + result);
	}
}
